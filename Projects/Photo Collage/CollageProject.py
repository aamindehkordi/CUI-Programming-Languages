import image
import math
import random
import sys
if len(sys.argv[1]) < 4:
    print("Incorrect filename, please try again :)")
else:
    fileName = sys.argv[1]
originalImage = image.FileImage(fileName)
width = originalImage.getWidth()
height = originalImage.getHeight()

one = image.EmptyImage(width, height)
two = image.EmptyImage(width, height)
three = image.EmptyImage(width, height)
four = image.EmptyImage(width, height)
six = image.EmptyImage(width, height)
seven = image.EmptyImage(width, height)
eight = image.EmptyImage(width, height)
nine = image.EmptyImage(width, height)

#Horizontal Flip
last = width - 1
for row in range(height):
       for col in range(width):
            pixel = originalImage.getPixel(last-col,row)
            one.setPixel(col, row, pixel)
            
#Sepia Filter
def convertToSepia(pixel):
    newR = int((pixel.getRed()*0.393 + pixel.getGreen()*0.769 + pixel.getBlue()*0.189))
    newR = min(newR,255)
    
    newG = int((pixel.getRed()*0.349 + pixel.getGreen()*0.686 + pixel.getBlue()*0.168))
    newG = min(newG,255)
    
    newB = int((pixel.getRed()*0.272 + pixel.getGreen()*0.535 + pixel.getBlue()*0.131))
    newB = min(newB,255)
    
    return image.Pixel(newR,newG,newB)
    
for row in range(height):                                   
        for col in range(width):                                
            pixel = originalImage.getPixel(col, row)
            pixel = convertToSepia(pixel)
            two.setPixel(col, row, pixel)
            
#Horizontal Mirror
last = width - 1
for row in range(height):
    for col in range(width//2):
            pixel = originalImage.getPixel(col,row)
            three.setPixel(col, row, pixel)
            three.setPixel(last-col,row,pixel)
            
#Grayscale Filter
def convertToGrayscale(originalImage):
    modifiedImage = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            pixel = originalImage.getPixel(col, row)
            pixelIntensity = pixel.getRed() + pixel.getGreen() + pixel.getBlue()
            avgRGB = pixelIntensity // 3
            pixel = image.Pixel(avgRGB, avgRGB, avgRGB)            
            modifiedImage.setPixel(col, row, pixel)
    return modifiedImage
    
four = convertToGrayscale(originalImage)

#Original Image

five = image.FileImage(fileName)

#Negative Filter
def convertPixelToNegative(pixel):
    newRed   = 255 - pixel.getRed()
    newGreen = 255 - pixel.getGreen()
    newBlue  = 255 - pixel.getBlue()
    return image.Pixel(newRed, newGreen, newBlue)
    
for row in range(height):                                   
        for col in range(width):                                
            pixel = originalImage.getPixel(col, row)
            pixel = convertPixelToNegative(pixel)
            six.setPixel(col, row, pixel)
            
#Edge Detection Filter
grayscaleImg = [[sum(originalImage.getPixel(x,y))//3 for y in range(height)]for x in range(width)]
black = image.Pixel(0, 0, 0)
white = image.Pixel(255, 255, 255)

xMask = [ [-1, -2, -1], [0, 0, 0], [1,2,1] ]
yMask = [ [1, 0, -1], [2, 0, -2], [1,0,-1] ]

kLength = len(yMask)

offset = kLength//2

for row in range(width):
    for col in range(height):
        rgbX = 0
        rgbY = 0
        for offX in range(kLength):
            for offY in range(kLength):
                x = row - offset + offX
                y = col - offset + offY

                x = max(x,0)
                x = min(x, width-1)
                y = max(y,0)
                y = min(y, height-1)

                rgbX += grayscaleImg[x][y] * xMask[offX][offY]
                rgbY += grayscaleImg[x][y] * yMask[offX][offY]

        newRGB = int(math.sqrt(rgbX**2 + rgbY**2))
        newRGB = min(newRGB,255)

        pixel = image.Pixel(newRGB,newRGB,newRGB)
        seven.setPixel(row,col,pixel)
        
#Random Drug Trip
for row in range(height):                                   
        for col in range(width):                                
            pixel = originalImage.getPixel(col, row)
            r = pixel.getRed() + random.randint(0,50) if pixel.getRed() < 206 else 255
            g = pixel.getGreen() - random.randint(0,50) if pixel.getGreen() > 49 else 0
            b = pixel.getBlue()  - random.randint(0,50) if pixel.getBlue() > 49 else 0
            pixel = image.Pixel(r, g, b)
            eight.setPixel(col, row, pixel)
        
#Blur Filter
mask = [  [2, 5, 2],
          [5, 2, 5],
          [2, 5, 2]  ]
maskSum = 30
kLength = len(mask)
offset = kLength//2

for row in range(height):                                   
    for col in range(width):

        r = 0
        g = 0
        b = 0

        for kX in range(kLength):
            for kY in range(kLength):
                x = col - offset + kX
                y = row - offset + kY

                x = max(x,0)
                x = min(x, width-1)
                y = max(y,0)
                y = min(y, height-1)
                
                
                pixel = originalImage.getPixel(x, y)
                
                r += mask[kX][kY] * pixel.getRed()    
                g += mask[kX][kY] * pixel.getGreen()  
                b += mask[kX][kY] * pixel.getBlue()   

        r = int(r/maskSum)
        g = int(g/maskSum)
        b = int(b/maskSum)
        r = min(r,255)
        g = min(g,255)
        b = min(b,255)

        pixel = image.Pixel(r, g, b)

        nine.setPixel(col, row, pixel)
        
#Creating the Collage
finW = (width*3) +20
finH = (height*3)+20
finalWindow = image.ImageWin(finW, finH, "Photo Collage")

one.setPosition((0*width)+(5),(0*height)+(5))
two.setPosition((1*width)+(10),(0*height)+(5))
three.setPosition((2*width)+(15),(0*height)+(5))
four.setPosition((0*width)+(5),(1*height)+(10))
five.setPosition((1*width)+(10),(1*height)+(10))
six.setPosition((2*width)+(15),(1*height)+(10))
seven.setPosition((0*width)+(5),(2*height)+(15))
eight.setPosition((1*width)+(10),(2*height)+(15))
nine.setPosition((2*width)+(15),(2*height)+(15))

one.draw(finalWindow)
two.draw(finalWindow)
three.draw(finalWindow)
four.draw(finalWindow)
five.draw(finalWindow)
six.draw(finalWindow)
seven.draw(finalWindow)
eight.draw(finalWindow)
nine.draw(finalWindow)

finalWindow.exitonclick()