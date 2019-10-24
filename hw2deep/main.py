import numpy as np
from PIL import Image
import os,glob
from math import exp
from sklearn.utils import shuffle

rng = 128 * 128 + 1 
size = [128, 128]

def trainPerceptron(inputs, t, weights, rho, iterNo):
     
    for j in range(iterNo):
        
        ##  Forward Propagation
        a = 0
        a = np.dot(weights, inputs)
        y = sigmoid(a)
        ##  End - Forward Propagation
                
        ##  Backward Propagation
        error = t - y       
        deltaW = np.zeros(rng)      
        DsigmoidF = Dsigmoid(y)
        deltaW = np.multiply((rho * error *  DsigmoidF), inputs)
        weights = weights + deltaW
        ##  End - Backward Propagation
         
    return weights

    
def sigmoid(x):
    return  (1 / (1 + exp(-1 * x)))

def Dsigmoid(x):
    sigmoidf = sigmoid(x)
    return  (1 - sigmoidf)*sigmoidf
    
def testPerceptron(sample_test, weights):
    a=0
    a = np.dot(weights, sample_test)
    result = sigmoid(a)    
    return result
def main():    
   
    trainCannonpath = ".\\train\\cannon"
    trainCellpath = ".\\train\\cellphone"
    
    rho = 0.001 
    weights = np.random.rand(rng)
    weights = weights / 100

    fileLen = len(glob.glob(os.path.join(trainCannonpath, '*.jpg')))
    fileLen = fileLen + len(glob.glob(os.path.join(trainCellpath, '*.jpg')))
    
    j = 0
    trainimages = np.zeros([fileLen, rng])
    trainresult = np.zeros([fileLen])
    
    for filename in glob.glob(os.path.join(trainCannonpath, '*.jpg')): 
        img = Image.open(filename).convert('L')
        img = img.resize(size, Image.ANTIALIAS)
        pxels = img.getdata()
        pxels = np.array(pxels)
        pxels = pxels.astype('float32')
        pxels = pxels / 255.0
        pxels = np.append(pxels, [1])
        trainimages[j] = pxels
        trainresult[j] =  0
        j = j + 1
    for filename in glob.glob(os.path.join(trainCellpath, '*.jpg')): 
        img = Image.open(filename).convert('L')
        img = img.resize(size, Image.ANTIALIAS)
        pxels = img.getdata()
        pxels = np.array(pxels)
        pxels = pxels.astype('float32')
        pxels = pxels / 255.0
        pxels = np.append(pxels, [1])
        trainimages[j] = pxels
        trainresult[j] =  1
        j = j + 1
    trainimages, trainresult = shuffle(trainimages, trainresult)
    
    for i in range(fileLen): 
        weights = trainPerceptron(trainimages[i], trainresult[i], weights, rho, 1000)

    testCannonPath = ".\\test\\cannon"
    testCellPath = ".\\test\\cellphone"
    
    for filename in glob.glob(os.path.join(testCannonPath, '*.jpg')): 
        img = Image.open(filename).convert('L')
        img = img.resize(size, Image.ANTIALIAS)
        pxels = img.getdata()
        pxels = np.array(pxels)
        pxels = pxels.astype('float32')
        pxels = pxels / 255.0
        pxels = np.append(pxels, [1])
        result = testPerceptron(pxels, weights)
        print("Cannon Test result : ", result)        
    for filename in glob.glob(os.path.join(testCellPath, '*.jpg')): 
        img = Image.open(filename).convert('L')
        img = img.resize(size, Image.ANTIALIAS)
        pxels = img.getdata()
        pxels = np.array(pxels)
        pxels = pxels.astype('float32')
        pxels = pxels / 255.0
        pxels = np.append(pxels, [1])
        result = testPerceptron(pxels, weights)
        print("Cellphone Test result : " , result)
 

if __name__ == '__main__':
    main()