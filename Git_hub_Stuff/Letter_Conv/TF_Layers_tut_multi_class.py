#we will need some of these packages at varoius points
import numpy as np
import os
from scipy.misc import imread,imsave
from scipy import ndimage
from skimage.transform import resize
import tensorflow as tf
from weighted_levenshtein import lev
from scipy import linalg as la

"""
This code processes images of handwritten letters and creates a CNN to classify these images
We include every lower case letter as well as select upper case letters
In addition the model will be trained to recognize various types of images that are not letters such as empty images, and images that only have straight lines
"""

#use this dictionary to decode the various  letters
#big_ indicates upper case
label_dict={'a':0,'b':1,'biga':2,'bigb':3,'bigd':4,'bige':5,'bigg':6,
                'bigh':7,'bigi':8,'bigl':9,'bigr':10,'bigt':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,
                'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,
                'v':31,'w':32,'x':33,'y':34,'z':35,'borders':36,'empty':37,}
                
inverse_dict={a:b for b,a in label_dict.items()}



def load_data(data_directory,preprocessed=True):
    #takes a directory with subfolders and each subfolder will contain examples of our classes as given in our dictionary above
    #also takes preprocessed which is a boolean defaulting to True, if False, we will also resize all the images and perform the sobel transformation
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if f.endswith(".jpg")]
        for f in file_names:
            next=imread(f)
            try:
                if preprocessed:
                    labels.append(label_dict[d])
                    if len(next.shape)==3:
                        images.append(np.expand_dims(next.mean(axis=2),2))
                    else:
                        images.append(np.expand_dims(next,2))
                else:
                    labels.append(label_dict[d])
                    if len(next.shape)==3:
                        images.append(np.expand_dims(resize(sobel(next.mean(axis=2)),(48,48),mode='constant',cval=0.0),2))
                    else:
                        images.append(np.expand_dims(resize(sobel(next),(48,48),mode='constant',cval=0.0),2))
            except KeyError:
                raise ValueError('Labels must be on the authority list, see label_dict')
    return np.array(images)/255, np.array(labels)
    
    
    
    
def model(features,labels,mode):
    #this function defines a custom model
    input_layer = tf.reshape(features["x"], [-1, 48, 48, 1])#48x48
    #perform convolutions with relu at the end of each convolution and some dropout, then pooling
    conv1 = tf.layers.conv2d(
      inputs=input_layer,
      filters=24,
      kernel_size=[7, 7],
      padding="same",
      activation=tf.nn.relu)
    
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)#24x24
    dropoutp1=tf.layers.dropout(inputs=pool1,rate=0.05,training=mode==tf.estimator.ModeKeys.TRAIN)
    
    conv2 = tf.layers.conv2d(
      inputs=dropoutp1,
      filters=36,
      kernel_size=[4, 4],
      padding="same",
      activation=tf.nn.relu)
  
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)#12x12
    dropoutp2=tf.layers.dropout(inputs=pool2,rate=0.6,training=mode==tf.estimator.ModeKeys.TRAIN)
    
    conv3 = tf.layers.conv2d(
      inputs=dropoutp2,
      filters=54,
      kernel_size=[3,3],
      padding="same",
      activation=tf.nn.relu)
      
    pool3 = tf.layers.max_pooling2d(inputs=conv3, pool_size=[2,2], strides=2)#6x6
    dropoutp3=tf.layers.dropout(inputs=pool3,rate=0.07,training=mode==tf.estimator.ModeKeys.TRAIN)
    
    conv4 = tf.layers.conv2d(
      inputs=dropoutp3,
      filters=81,
      kernel_size=[3,3],
      padding="same",
      activation=tf.nn.relu)
      
    pool4 = tf.layers.max_pooling2d(inputs=conv4, pool_size=[2,2], strides=2)#3x3
    dropoutp4=tf.layers.dropout(inputs=pool4,rate=0.1,training=mode==tf.estimator.ModeKeys.TRAIN)
    
    #flatten the images which are 3x3 but is also 81 units deep (because our last convolution layer had 81 filters) to give total length of 3*3*81
    pool4_flat=tf.reshape(dropoutp4, [-1,3*3*81])
    #define our dense layer
    dense=tf.layers.dense(inputs=pool4_flat,units=512,activation=tf.nn.relu)
    #do one final dropout, this time much more dropout than we saw earlier
    dropout=tf.layers.dropout(inputs=dense,rate=0.4,training=mode==tf.estimator.ModeKeys.TRAIN)
    
    #one_hot encode the results
    logits=tf.layers.dense(inputs=dropout,units=37)
    
    ones=np.ones(37)
    arange=np.arange(37)
    predictions={
      "classes":tf.argmax(input=logits,axis=1),
      "probabilities":tf.nn.softmax(logits,name="softmax_tensor")
      }
    
    #perform the operations appropriate for the mode we are in
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode,predictions=predictions)
    
    labels_one_hot=tf.one_hot(indices=tf.cast(labels, tf.int32), depth=45)
    loss = tf.losses.softmax_cross_entropy(onehot_labels=labels_one_hot, logits=logits)
    
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer=tf.train.GradientDescentOptimizer(learning_rate=.00015)
        train_op = optimizer.minimize(
          loss=loss,
          global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)
    if mode == tf.estimator.ModeKeys.EVAL:
        eval_metric_ops = {
          "accuracy": tf.metrics.accuracy(
          labels=labels, predictions=predictions["classes"])}
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)
        
def get_feature_dict(images,labes):
    #simply makes a dictionary mapping input (x's) to correct output (y's)
    return {"x":images,"y":labels}
        
def train(train_folder,eval_folder,model_folder,batch_size,steps,preprocessed=True):
    #we take a a folder with images to train on
    #a folder to evaluate our model with
    #and a folder to save our model in, if this folder already has a model it will attempt to restore that model
    #Raises an error if the model folder contains a model that does not match the format defined in our model function
    
    
    train_data,train_labels = load_data(train_folder,preprocessed) # Returns np.array
    eval_data,eval_labels = load_data(eval_folder,preprocessed) # Returns np.array
    classifier= tf.estimator.Estimator(model_fn = model, model_dir = model_folder)#defined using our model function above
    tensors_to_log = {"probabilities": "softmax_tensor"}
    logging_hook = tf.train.LoggingTensorHook(tensors=tensors_to_log, every_n_iter=50)#we can see the above log results for every 50 steps during training
    # Train the model
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": train_data},
        y=train_labels,
        batch_size=batch_size,
        num_epochs=None,
        shuffle=True)
    classifier.train(
        input_fn=train_input_fn,
        steps=steps,
        hooks=[logging_hook])
    
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data},
        y=eval_labels,
        num_epochs=1,
        shuffle=False)
    eval_results = classifier.evaluate(input_fn=eval_input_fn)
    print(eval_results)
    
def predict(image,model_folder):
    #this model takes an image and a folder with a trained model and makes a prediction using the model
    classifier= tf.estimator.Estimator(model_fn = model, model_dir = model_folder)
    tensors_to_log = {"probabilities": "softmax_tensor"}
    logging_hook = tf.train.LoggingTensorHook(
        tensors=tensors_to_log, every_n_iter=50)

    # predict with the model and print results
    pred_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": image},
        shuffle=False)
    pred_results = list(classifier.predict(input_fn=pred_input_fn))
    return [p['classes'] for p in pred_results],[p['probabilities'] for p in pred_results]

    
def sobel(image):
    #performs the sobel transformation on an image
    dx=ndimage.sobel(image,1)
    dy=ndimage.sobel(image,0)
    mag=np.hypot(dx,dy)
    return mag
    
    
    

    
def levenshtein_weighted(pred_str,test_str,sub_mat,ins_cost=1,del_cost=1):
    #finds the levenshtein distance between two words
    #levenshtein distance essentially measures the number of insertions, deletions and substituion necessary to change one word into another
    #levenshtein distance is zero IFF the two words are identical or insertion/deletion/substitution costs are zero
    #input are the two strings to compare, a matrix of weights for substitution, and insertion/deletion costs which both default to one
    #note L(s1,s2)==L(s2,s1) may not be true if the substituion matrix is not symmetric
    
    #for our letter dictionary we only need the letters our model is trained to identify
    let_dict={'a':0,'b':1,'A':2,'B':3,'D':4,'E':5,'G':6,
                'H':7,'I':8,'L':9,'R':10,'T':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,
                'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,
                'v':31,'w':32,'x':33,'y':34,'z':35,' ':37}
    #if either string is now empty (base case) we just delete or insert as necessary
    if len(pred_str)==0:
        return len(test_str)*del_cost
    if len(test_str)==0:
        return len(pred_str)*ins_cost
    cost=sub_mat[let_dict[pred_str[-1]],let_dict[test_str[-1]]]
    #use recursion until we reach the base case
    return min([levenshtein_w_mod_dis(pred_str[:len(pred_str)-1],test_str,dis_mat)+del_cost,
                levenshtein_w_mod_dis(pred_str,test_str[:len(test_str)-1],dis_mat)+ins_cost,
                levenshtein_w_mod_dis(pred_str[:len(pred_str)-1],test_str[:len(test_str)-1],dis_mat)+cost])
                
                
def identify_full(letters,model_folder,possibilities,sub_mat,ins_cost=1,del_cost=1):
    #take a sequence of images, a model folder, and possible strings that our sequence of images may match to
    #find the string from the possibilities that is most likely what our lsit of images maps to
    let_dict={'a':0,'b':1,'A':2,'B':3,'D':4,'E':5,'G':6,
                'H':7,'I':8,'L':9,'R':10,'T':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,
                'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,
                'v':31,'w':32,'x':33,'y':34,'z':35,' ':37}
    inverse_let_dict={a:b for b,a in let_dict.items()}
    pred_list=predict(letters,model_folder)[0]
    pred_str=''
    for i in pred_list:
        try:
            pred_str+=inverse_let_dict[i]
        except KeyError:
            None
    return possibilities[np.argmin(np.array([levenshtein_weighted(pred_str,test,sub_mat,ins_cost,del_cost) for test in possibilities]))]
                
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    