# define image object
# this creates the object but does not draw it to canvas
myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

# get the size of the image using the ImageObject’s .size() method
print(myImage.size())
# set the canvas size to the image size (unpacking the size tuple)
newPage(*myImage.size())
# draw the image to the canvas from the lower left corner
image(myImage, (0, 0))