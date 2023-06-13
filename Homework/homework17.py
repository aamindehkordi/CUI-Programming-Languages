import image
import sys
def scale_image(originalImage, scale):
    
    width  = originalImage.getWidth()
    height = originalImage.getHeight()
    
    scaledImg = image.EmptyImage(width*scale, height*scale)    
    for row in range(height):
        for col in range(width):
            
            pixel = originalImage.getPixel(col, row)
            
            scaledImg.setPixel(scale*col,   scale*row, pixel)
            scaledImg.setPixel(scale*col+1, scale*row, pixel)
            scaledImg.setPixel(scale*col,   scale*row+1, pixel)
            scaledImg.setPixel(scale*col+1, scale*row+1, pixel)
    
    return scaledImg

def enlarge_image(fileName):
    scale = sys.argv[0]
    
    originalImage = image.FileImage(fileName)
    width = originalImage.getWidth()
    height = originalImage.getHeight()
    
    scaledImg = scale_image(originalImage, scale)
    scaledImg.setPosition(0, height+1)
    
    window = image.ImageWin(width * scale, height * 3, "{}x bigger".format(scale))
    originalImage.draw(window)
    scaledImg.draw(window)
    
def reduce_size(fileName):
    scale = sys.argv[0]
    
    originalImage = image.FileImage(fileName)
    width = originalImage.getWidth() // scale
    height = originalImage.getHeight() // scale
    reducedImg = image.EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            pix1 = originalImage.getPixel(scale*col,   scale*row)
            pix2 = originalImage.getPixel(scale*col+1, scale*row)
            pix3 = originalImage.getPixel(scale*col,   scale*row+1)
            pix4 = originalImage.getPixel(scale*col+1, scale*row+1)
            red = (pix1.getRed() + pix2.getRed() + pix3.getRed() + pix4.getRed()) // 4
            blue = (pix1.getBlue() + pix2.getBlue() + pix3.getBlue() + pix4.getBlue()) // 4
            green = (pix1.getGreen() + pix2.getGreen() + pix3.getGreen() + pix4.getGreen()) // 4
            reducedImg.setPixel(col,row,image.Pixel(red,green,blue))
            
    reducedImg.setPosition(0, height+1)
    
    window = image.ImageWin(width*scale, height*scale, "{}x smaller".format(scale)) # I am not sure on how to make them fit like the ones above, also this is mostly from the book, I can admit that what I tried did not work.
    originalImage.draw(window)
    reducedImg.draw(window)