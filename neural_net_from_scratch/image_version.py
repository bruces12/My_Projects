import numpy as np

def data(num_samps,w1,w2):
    x=np.random.randn(num_samps,100)
    return x, get_y(x,w1,w2)
    
def get_y(x,w1,w2):
    y=np.exp(w1*x.T).T @ w2
    return y
    
def make_image(sample):
    height=[0]
    for i in sample:
        height.append(int(height[-1]+10*i))
    height=np.array(height)-min(height)
    height=(100*height/max(height)).astype('int')
    rows=max(height)
    image=np.zeros((rows,len(sample)))
    for i in range(len(height)-1):
        top=max(height[i-1],height[i])
        bot=min(height[i-1],height[i])
        image[bot:top,i]=1
    return image