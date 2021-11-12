myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

myWidth, myHeight = myImage.size()
newPage()

myMultiplier = width()/myWidth
if myMultiplier > 1:
    myMultiplier = 1

scale(myMultiplier)

#myImage.sepiaTone()
myImage.vignette(1000, 0)
image(myImage, (0, 0))
myImage.colorPosterize(5)
blendMode('colorDodge')
image(myImage, (0, 0), alpha=1)