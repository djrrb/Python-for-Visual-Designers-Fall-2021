myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

myWidth, myHeight = myImage.size()
newPage(100, 100)
print(myWidth, width(), width()/myWidth)
myMultiplier = width()/myWidth
if myMultiplier > 1:
    myMultiplier = 1

scale(myMultiplier)
image(myImage, (0, 0))