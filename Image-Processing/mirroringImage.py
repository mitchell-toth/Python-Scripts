from image import *

def mirror(imageFile):
    oldImage = FileImage(imageFile)  #get old image
    width = oldImage.getWidth() 
    height = oldImage.getHeight()
    #make window double as wide
    myImageWindow = ImageWin("Image Processing", width*2, height)
    oldImage.draw(myImageWindow)  #draw old image normally
    newIm = EmptyImage(width,height)  #make new, empty image
    for row in range(height):  #manipulate new image
        offset = 1
        for col in range(width//2,width):
            originalPixel = oldImage.getPixel(col,row)
            newIm.setPixel(col,row,originalPixel)
            newIm.setPixel(col-offset,row,originalPixel)
            offset += 2
    newIm.setPosition(width + 1, 0)  #move new image
    newIm.draw(myImageWindow)  #draw new image
    myImageWindow.exitOnClick()


mirror("pencils.gif")
