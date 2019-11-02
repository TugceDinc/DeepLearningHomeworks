import matplotlib.pyplot as plt
from PIL import Image

def leftby90degree(image):
    imWidth, imHeight = image.size
    pixelMap = image.load()
    img = Image.new( image.mode, [imHeight, imWidth])
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixelsNew[i, j] = pixelMap[imWidth - j - 1, i]
    return img

def rightby90degree(image):
    imWidth, imHeight = image.size
    pixelMap = image.load()
    img = Image.new(image.mode, [imHeight, imWidth])
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixelsNew[i, j] = pixelMap[j, imHeight - i - 1]
    return img

def flipsimagevertically(image):
    imWidth, imHeight = image.size
    pixelMap = image.load()
    img = Image.new( image.mode, [imWidth, imHeight])
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixelsNew[i, j] = pixelMap[i, imHeight- 1 - j]
            
    return img
    

def flipsimagehorizantally(image):
    imWidth, imHeight = image.size
    pixelMap = image.load()
    img = Image.new( image.mode, [imWidth, imHeight])
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixelsNew[i, j] = pixelMap[imWidth - i - 1, j]
            
    return img

def resizesinputimagetohalf(image):
    imWidth, imHeight = image.size
    pixelMap = image.load()
    img = Image.new( image.mode, [imWidth//2, imHeight//2])
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            sum1 = [0,0,0,255]
            for k in range(i*2, i*2 + 2):
                for l in range(j*2, j*2 + 2):
                    temp = pixelMap[k, l]
                    temp = list(temp)
                    sum1[0] = sum1[0] + temp[0]
                    sum1[1] = sum1[1] + temp[1]
                    sum1[2] = sum1[2] + temp[2]
            sum1[0] = sum1[0] //4
            sum1[1] = sum1[1] //4
            sum1[2] = sum1[2] //4
            pixelsNew[i, j] = tuple(sum1)
            
    return img

def main():
    img = Image.open('cat.png')
    img = img.convert('RGB')
    titles = ['Original Image', 'flips cat image vertically',
            'flips cat image horizontally', 'rotates cat image to left by 90 degree', 'rotates cat image to right by 90 degree',
            'resizes input image to half by keeping aspect ratio' ]
    imghorizantal = flipsimagehorizantally(img)
    
    imgvertical = flipsimagevertically(img)
    imgleft =  leftby90degree(img)
    imgright = rightby90degree(img)
    imghalf = resizesinputimagetohalf(img)

    images = [img, imgvertical, imghorizantal, imgleft, imgright, imghalf]
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i]),plt.xticks([]),plt.yticks([])
    plt.show()
        
if __name__ == '__main__':
    main()

