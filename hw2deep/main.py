import numpy as np
from PIL import Image
import os,glob
#import matplotlib.pyplot as plt
#from sklearn.utils import shuffle
from math import exp

def trainPerceptron(inputs, t, weights, rho, iterNo):
    rng = 128 * 128 + 1  
    for j in range(iterNo):
        
        ##Forward Propagation
        a = 0
        for i in range(rng) :
            a = a + weights[i]*inputs[i]
            
        y = sigmoid(a)
        ##End - Forward Propagation
        
        ##Backward Propagation
        error = t - y        
        deltaW = np.zeros(rng)        
        for i in range(rng) :
            deltaW[i] = rho * error * inputs[i]
        for i in range(rng) :
            weights[i] = weights [i] - inputs[i]
        ##End - Backward Propagation
        
    return weights

    
def sigmoid(x):
    return  (1 / (1 + exp(-1*x)))
    
#def testPerceptron(sample_test, weights):
    
def main():    
    size = [255,255]
    trainCannonpath = ".\\train\\cannon"
    trainCellpath = ".\\train\\cellphone"
    
    rho = 0.001
    rng = 128 * 128 + 1  
    weights = np.random.rand(rng)
    
    for filename in glob.glob(os.path.join(trainCannonpath, '*.jpg')): 
        img = Image.open(filename).convert('LA')
        img = img.resize(size, Image.ANTIALIAS)
        pxels = img.getdata()
        pxels = np.array(pxels)
        pxels = np.append(pxels, [1])
        weights = trainPerceptron(pxels, 0, weights, rho, 1000)
        
    for filename in glob.glob(os.path.join(trainCellpath, '*.jpg')): 
        img = Image.open(filename).convert('LA')
        img = img.resize(size, Image.ANTIALIAS)
        pxels = img.getdata()
        pxels = np.array(pxels).reshape(img.size[0], img.size[1])
        pxels = np.append(pxels, [1])
        weights = trainPerceptron(pxels, 0, weights, rho, 1000)
    

if __name__ == '__main__':
    main()