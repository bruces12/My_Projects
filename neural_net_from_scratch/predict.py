import numpy as np

#sigmoid function for use throughout
sig=lambda x:np.exp(x)/(1+np.exp(x))



def predict(l4,w5):
    """
    calculates the ooutput of the final layer, ie the prediction of the model
    parameters:
        l4: ndarray(,n) the output of the fourth layer
        w5: ndarray(,n) the weights for the fifth layer
    returns:
        prediction: float, the final prediction of the neura network
    """
    return np.dot(l4,w5)
    
def pred4(l3,w4):
    """
    calculates the fourth layer of the network
    parameters:
        l3, ndarray(,n) the output of layer three
        w4, ndarray(m,n) the weights of the fourth layer
    return l4, ndarray(,m) the fourth layer of the network
    """
    return np.exp(-(w4 @ l3)**2)
    
def pred3(l2,w3):
    """
    calculates the third layer of the network
    parameters:
        l2, ndarray(,n) the output of layer two
        w3, ndarray(m,n) the weights of the third layer
    return l3, ndarray(,m) the third layer of the network
    """
    return sig(w3 @ l2)
    
def pred2(l1,w2):
    """
    calculates the second layer of the network
    parameters:
        l1, ndarray(,n) the output of layer one
        w2, ndarray(m,n) the weights of the second layer
    return l2, ndarray(,m) the fourth layer of the network
    """
    return np.sqrt(w2**2 @ l1**2)

def pred1(x,w1):
    """
    calculates the first layer of the network
    parameters:
        x, ndarray(,n) the input we are trying to predict for
        w1, ndarray(m,n) the weights of the first layer
    return l1, ndarray(,m) the first layer of the network
    """
    return np.exp(w1*x)

def dw5(l5,l4,rets):
    """
    calculates the gradient of the squared error with respect to the fifth layer weights
    parameters:
        l5, ndarray(,m) the output of layer five, or the prediction
        l4, ndarray(,n) the output of layer four
        rets, the true value we want to see the model return
    return dw5, the gradient of the squared error with respect to the fifth layer weights
    """
    return -2*(rets-l5)*l4
    
def dw4(l5,l4,l3,r,w5,w4):
    """
    calculates the gradient of the squared error with respect to the fourth layer weights
    parameters:
        l5, float the output of layer five, or the prediction
        l4, ndarray(,n) the output of layer four
        l3, ndarray(,p) the output of the third layer
        r, float, the true value we want to see the model return
        w5, ndarray(,n) the weights of the fifth layer
        w4, ndarray(n,p) the current weights of the fourth layer
    return dw4, the gradient of the squared error with respect to the fifth layer weights
    """
    return -2*(r-l5)*np.outer((-2*w5*(w4 @ l3))*l4,l3)
    
def dw3(l5,l3,l2,w5,w4,w3,r):
    """
    calculates the gradient of the squared error with respect to the fourth layer weights
    parameters:
        l5, float the output of layer five, or the prediction
        l3, ndarray(,n) the output of the third layer
        l2, ndarray(,m) the output of the second layer
        w5, ndarray(,p) the weights of the fifth layer
        w4, ndarray(p,n) the current weights of the fourth layer
        w3, ndarray(n,m) the current weights of the third layer
        r, float, the true value we want to see the model return
    return dw4, the gradient of the squared error with respect to the fifth layer weights
    """
    grad=np.zeros_like(w3)
    w5=w5.reshape((10,1,1))
    dl4i=np.array([-2*(np.dot(w4[i],l3)*np.exp(-np.dot(w4[i],l3)**2))*(w4[i].reshape((20,1))*np.array([l2*np.exp(np.dot(w3[j],l2))/(1+np.exp(np.dot(w3[j],l2)))**2
                    for j in range(20)]))
                    for i in range(10)])
    return -2*(r-l5)*(w5*dl4i).sum(axis=0)
    
def dw2(l5,l3,l2,l1,w5,w4,w3,w2,r):
    """
    calculates the gradient of the squared error with respect to the fourth layer weights
    parameters:
        l5, float the output of layer five, or the prediction
        l3, ndarray(,n) the output of the third layer
        l2, ndarray(,m) the output of the second layer
        l1, ndarray(,q) the output of the first layer
        w5, ndarray(,p) the weights of the fifth layer
        w4, ndarray(p,n) the current weights of the fourth layer
        w3, ndarray(n,m) the current weights of the third layer
        w2, ndarray(m,q) the current weights of the second layer
        r, float, the true value we want to see the model return
    return dw4, the gradient of the squared error with respect to the fifth layer weights
    """
    dl2=np.array([(w2[i]*l1**2)/(np.sqrt(np.dot(w2[i]**2,l1**2))) for i in range(45)])#45x100
    dl3=np.array([(np.exp(np.dot(w3[i],l2))/(1+np.exp(np.dot(w3[i],l2)))**2)*w3[i].reshape((45,1))*dl2 for i in range(20)])#20x45,100
    dl4=-2*np.array([np.dot(w4[i],l3)*np.exp(-np.dot(w4[i],l3)**2)*(w4[i].reshape((20,1,1))*dl3).sum(axis=0) for i in range(10)])#10x45x100
    dl5=(w5.reshape(10,1,1)*dl4).sum(axis=0)#45*100
    return -2*(r-l5)*dl5#45x100
    
def dw1(l5,l3,l2,l1,x,w5,w4,w3,w2,w1,r):
    """
    calculates the gradient of the squared error with respect to the fourth layer weights
    parameters:
        l5, float the output of layer five, or the prediction
        l3, ndarray(,n) the output of the third layer
        l2, ndarray(,m) the output of the second layer
        l1, ndarray(,q) the output of the first layer
        x,  ndarray(,q) the input we are trying to predict for
        w5, ndarray(,p) the weights of the fifth layer
        w4, ndarray(p,n) the current weights of the fourth layer
        w3, ndarray(n,m) the current weights of the third layer
        w2, ndarray(m,q) the current weights of the second layer
        r, float, the true value we want to see the model return
    return dw4, the gradient of the squared error with respect to the fifth layer weights
    """
    dl1=x*np.exp(w1*x)#100*1
    dl2=np.array([w2[i]**2*l1*x*np.exp(w1*x)/np.sqrt(np.dot(w2[i]**2,l1**2)) for i in range(45)])
    #dl2=np.array([np.dot(w2[i]**2,l1)/np.sqrt(np.dot(w2[i]**2,l1**2))*dl1 for i in range(45)])#45x100
    dl3=np.array([((np.exp(np.dot(w3[i],l2))/(1+np.exp(np.dot(w3[i],l2)))**2)*w3[i].reshape((45,1))*dl2).sum(axis=0) for i in range(20)])#20x100
    dl4=-2*np.array([((w4[i]*l3).reshape((20,1))*np.exp(-np.dot(w4[i],l3)**2)*dl3).sum(axis=0) for i in range(10)])#10x100
    dl5=(w5.reshape(10,1)*dl4).sum(axis=0)#10*100
    return -2*(r-l5)*dl5#1x100
    
    

#calculates total loss of many variables with predictions and true values as inputs
loss = lambda x,y:np.sum((x-y)**2)

def preds(w1,w2,w3,w4,w5,xs):
    #returns the prediction of our neural network
    preds=[]
    for i in range(len(xs)):
        l1=pred1(xs[i],w1)
        l2=pred2(l1,w2)
        l3=pred3(l2,w3)
        l4=pred4(l3,w4)
        l5=predict(l4,w5)
        preds.append(l5)
    return np.array(preds)
    
def tot_loss(w1,w2,w3,w4,w5,xs,rs):
    #calculates total loss with weights and data as inputs
    x=preds(w1,w2,w3,w4,w5,xs)
    return loss(x,rs)

#the following function all numerically approximate the gradient of the loss with respect to weights on different levels
#these functions approximate by perturbing the current weights and checking how much the output changes
#they are too slow for any practical application, but can be used to verify our analytical solutions are accurate
def num_grad4(w1,w2,w3,w4,w5,x,y):
    grad_n=np.zeros_like(w4)
    l1=pred1(x,w1)
    l2=pred2(l1,w2)
    l3=pred3(l2,w3)
    l4=pred4(l3,w4)
    l5=predict(l4,w5)
    lo=loss(l5,y)
    for i in range(len(w4)):
        for j in range(len(w4[i])):
            pw4=np.copy(w4)
            pw4[i,j]+=1e-9
            l1p=pred1(x,w1)
            l2p=pred2(l1p,w2)
            l3p=pred3(l2p,w3)
            l4p=pred4(l3p,pw4)
            l5p=predict(l4p,w5)
            lp=loss(l5p,y)
            grad_n[i,j]=(lp-lo)/1e-9
    return grad_n
    
def num_grad3(w1,w2,w3,w4,w5,x,y):
    grad_n=np.zeros_like(w3)
    l1=pred1(x,w1)
    l2=pred2(l1,w2)
    l3=pred3(l2,w3)
    l4=pred4(l3,w4)
    l5=predict(l4,w5)
    lo=loss(l5,y)
    for i in range(len(w3)):
        for j in range(len(w3[i])):
            pw3=np.copy(w3)
            pw3[i,j]+=1e-8
            l1p=pred1(x,w1)
            l2p=pred2(l1p,w2)
            l3p=pred3(l2p,pw3)
            l4p=pred4(l3p,w4)
            l5p=predict(l4p,w5)
            lp=loss(l5p,y)
            grad_n[i,j]=(lp-lo)/1e-8
    return grad_n
    
def num_grad2(w1,w2,w3,w4,w5,x,y):
    grad_n=np.zeros_like(w2)
    l1=pred1(x,w1)
    l2=pred2(l1,w2)
    l3=pred3(l2,w3)
    l4=pred4(l3,w4)
    l5=predict(l4,w5)
    lo=loss(l5,y)
    #print(len(w2),len(w2[0]))
    for i in range(len(w2)):
        for j in range(len(w2[i])):
            pw2=np.copy(w2)
            pw2[i,j]+=1e-8
            l1p=pred1(x,w1)
            l2p=pred2(l1p,pw2)
            l3p=pred3(l2p,w3)
            l4p=pred4(l3p,w4)
            l5p=predict(l4p,w5)
            lp=loss(l5p,y)
            grad_n[i,j]=(lp-lo)/1e-8
    return grad_n
    
def num_grad1(w1,w2,w3,w4,w5,x,y):
    grad_n=np.zeros_like(w1)
    l1=pred1(x,w1)
    l2=pred2(l1,w2)
    l3=pred3(l2,w3)
    l4=pred4(l3,w4)
    l5=predict(l4,w5)
    lo=loss(l5,y)
    #print(len(w2),len(w2[0]))
    for i in range(len(w1)):
        pw1=np.copy(w1)
        pw1[i]+=1e-4
        l1p=pred1(x,pw1)
        l2p=pred2(l1p,w2)
        l3p=pred3(l2p,w3)
        l4p=pred4(l3p,w4)
        l5p=predict(l4p,w5)
        lp=loss(l5p,y)
        grad_n[i]=(lp-lo)/1e-4
    return grad_n
#this is the end of the functions that numerically approximate the gradients
    
def all_layers(x,w1,w2,w3,w4,w5):
    #returns each of the layers in our network
    l1=pred1(x,w1)
    l2=pred2(l1,w2)
    l3=pred3(l2,w3)
    l4=pred4(l3,w4)
    l5=predict(l4,w5)
    return l1,l2,l3,l4,l5
    
    
#Each of the following five functions takes the current weights, data, true values the data maps to
#and steps in the direction of the negative gradient to begin minimizing the loss function
#the functions also take step_size which is how far we move in the gradient direction
#batch_size, which is how many samples we want to use in finding the gradient at each step_size
#and epochs which gives how many times we want to step in the iterative process 
def opt5(w1,w2,w3,w4,w5,xs,rs,step_size=.01,batch_size=100,epochs=500):
    for j in range(epochs):
        idx=list(set(np.random.randint(0,len(xs),batch_size)))
        grad=np.zeros_like(w5)
        for i in idx:
            l1=pred1(xs[i],w1)
            l2=pred2(l1,w2)
            l3=pred3(l2,w3)
            l4=pred4(l3,w4)
            l5=predict(l4,w5)
            grad+=dw5(l5,l4,rs[i])
        w5-=grad*(step_size/len(xs))
        print(str(100*j//epochs)+'%',end='\r')
    return w5
    
def opt4(w1,w2,w3,w4,w5,xs,rs,step_size=.01,batch_size=100,epochs=500):
    for j in range(epochs):
        idx=list(set(np.random.randint(0,len(xs),batch_size)))
        grad=np.zeros_like(w4)
        for i in idx:
            l1=pred1(xs[i],w1)
            l2=pred2(l1,w2)
            l3=pred3(l2,w3)
            l4=pred4(l3,w4)
            l5=predict(l4,w5)
            grad+=dw4(l5,l4,l3,rs[i],w5,w4)
        w4-=grad*(step_size/len(xs))
        print(str(100*j//epochs)+'%',end='\r')
    return w4
    
def opt3(w1,w2,w3,w4,w5,xs,rs,batch_size=128,step_size=.01,epochs=500):
    for j in range(epochs):
        idx=list(set(np.random.randint(0,len(xs),batch_size)))
        grad=np.zeros_like(w3)
        for i in idx:
            l1=pred1(xs[i],w1)
            l2=pred2(l1,w2)
            l3=pred3(l2,w3)
            l4=pred4(l3,w4)
            l5=predict(l4,w5)
            grad+=dw3(l5,l3,l2,w5,w4,w3,rs[i])
        w3-=grad*(step_size/len(idx))
        print(str(100*j//epochs)+'%',end='\r')
    return w3
    
def opt2(w1,w2,w3,w4,w5,xs,rs,batch_size=64,step_size=.01,epochs=500):
    for j in range(epochs):
        idx=list(set(np.random.randint(0,len(xs),batch_size)))
        grad=np.zeros_like(w2)
        for i in idx:
            l1=pred1(xs[i],w1)
            l2=pred2(l1,w2)
            l3=pred3(l2,w3)
            l4=pred4(l3,w4)
            l5=predict(l4,w5)
            grad+=dw2(l5,l3,l2,l1,w5,w4,w3,w2,rs[i])
        w2-=grad*(step_size/len(idx))
        print(str(100*j//epochs)+'%',end='\r')
    return w2
    
def opt1(w1,w2,w3,w4,w5,xs,rs,batch_size=64,step_size=.01,epochs=500):
    for j in range(epochs):
        idx=list(set(np.random.randint(0,len(xs),batch_size)))
        grad=np.zeros_like(w1)
        for i in idx:
            l1=pred1(xs[i],w1)
            l2=pred2(l1,w2)
            l3=pred3(l2,w3)
            l4=pred4(l3,w4)
            l5=predict(l4,w5)
            grad+=dw1(l5,l3,l2,l1,xs[i],w5,w4,w3,w2,w1,rs[i])
        w1-=grad*(step_size/len(idx))
        print(str(100*j//epochs)+'%',end='\r')
    return w1
    
    


























