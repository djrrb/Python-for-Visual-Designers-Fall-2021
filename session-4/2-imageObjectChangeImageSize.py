# create an instance of ImageObject pointing to the kitten
myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

# this time we will scale the image to fit the existing canvas
myWidth, myHeight = myImage.size()

# make a canvas
newPage("Letter")

print(myWidth, width(), width()/myWidth)

# figure out what we have to scale by to get the image to fit
# divide the width of the canvas by the width of the image
myMultiplier = width()/myWidth
# clamp myMultiplier so that it won’t scale the image up, only down
if myMultiplier > 1:
    myMultiplier = 1

# scale the canvas
scale(myMultiplier)
# draw the image
image(myImage, (0, 0))