# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image

# open the image
myimage = Image.open('834392.jpg')

# show the image
myimage.show()

# my cropped image
mybox = (330 ,  300 , 800 , 800)

mynewimage = myimage.crop(mybox)

mynewimage.show()

# my converted mode
myconverted = myimage.convert('L')
myconverted.crop(mybox).show()

