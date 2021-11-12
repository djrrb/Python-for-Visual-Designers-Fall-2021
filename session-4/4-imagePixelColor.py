# make an image object
myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

# draw the image to canvas
image(myImage, (0, 0))

# ask the image what the color is at certain coordinates
myEyedropperColor = imagePixelColor(myImage, (500, 300)

# set the fill color, unpacking the myEyedropperColor tuple
fill(*myEyedropperColor))

# draw a rectangle in that color
rect(0, 0, 500, 500)