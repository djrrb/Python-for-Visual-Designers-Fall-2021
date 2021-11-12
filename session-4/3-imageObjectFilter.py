# make an image object
myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

# query the image object for its size
myWidth, myHeight = myImage.size()

# make a new page
newPage()

# get the multiplier that will scale the image to fit the page
myMultiplier = width()/myWidth
# don’t let the image scale up by overriding the myMultiplierVariable and setting it to 1 anytime it is over 1
if myMultiplier > 1:
    myMultiplier = 1

# scale the canvas
scale(myMultiplier)

# apply some filters
myImage.sepiaTone()
myImage.vignette(1000, 0)

# now draw the image
image(myImage, (0, 0))

# hey we can even layer them
# apply some more filters
myImage.colorPosterize(5)

# change the blend mode so the images interact
# this will multiply out the light colors
blendMode('colorDodge')

# draw the image again, because why not!
image(myImage, (0, 0), alpha=1)