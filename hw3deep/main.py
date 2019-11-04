
import numpy as np
from PIL import Image
import os,glob
from sklearn.utils import shuffle
import pandas as pd

rng = 128 * 128 
size = [128, 128]

def KNN(x_train, y_train, sample_test, k ):
    
    lenght = len(x_train)
    
    Result = np.zeros([lenght, 2])
    print(len(Result))
    for i in range(lenght):
        xxxx = x_train[i]
        result = np.subtract(sample_test, xxxx)
        result = np.square(result)
        result = np.sum(result)
        result = np.sqrt(result)
        Result[i,0] = result
        Result[i,1] = y_train[i]
    dataset = pd.DataFrame({'Column1': Result[:, 0], 'Column2': Result[:, 1]})
    Result = dataset.sort_values('Column1')
    for i in range(7):
        print(Result[i])
    return 0



def main():    
   
    trainButterflyPath = ".\\train\\butterfly"
    trainChairPath = ".\\train\\chair"
    trainLaptopPath = ".\\train\\laptop"
    

    fileLen = len(glob.glob(os.path.join(trainButterflyPath, '*.jpg')))
    fileLen = fileLen + len(glob.glob(os.path.join(trainChairPath, '*.jpg')))
    fileLen = fileLen + len(glob.glob(os.path.join(trainLaptopPath, '*.jpg')))
    
    j = 0
    trainimages = np.zeros([fileLen, rng])
    trainresult = np.zeros([fileLen])
    
    for filename in glob.glob(os.path.join(trainButterflyPath, '*.jpg')): 
        trainimages[j] = read128x128Image(filename)
        trainresult[j] = 1
        j = j + 1
    for filename in glob.glob(os.path.join(trainChairPath, '*.jpg')): 
        trainimages[j] = read128x128Image(filename)
        trainresult[j] = 2
        j = j + 1
    
    for filename in glob.glob(os.path.join(trainLaptopPath, '*.jpg')): 
        trainimages[j] = read128x128Image(filename)
        trainresult[j] = 3
        j = j + 1        

    trainimages, trainresult = shuffle(trainimages, trainresult)
    k = 7

    test = ".\\test"
    
    for filename in glob.glob(os.path.join(test, '*.jpg')): 
        pxels = read128x128Image(filename)  
        KNN(trainimages, trainresult, pxels, k )
    



def read128x128Image(filename):
    img = Image.open(filename).convert('L')
    img = img.resize(size, Image.ANTIALIAS)
    pxels = img.getdata()
    pxels = np.array(pxels)
    pxels = pxels.astype('float32')
    pxels = pxels / 255.0
    return pxels


if __name__ == '__main__':
    main()    
    
    
    
