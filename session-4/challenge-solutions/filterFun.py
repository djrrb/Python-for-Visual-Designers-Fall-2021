# https://drawbot.com/content/image/imageObject.html

# define the image object
myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

# do some funky stuff
myImage.kaleidoscope(
    6, # number of sides
    (310, 800), # center of image
)

# Applies a preconfigured set of effects that imitate vintage photography film with emphasized cool colors.
myImage.photoEffectProcess()

# make a new page the size of the image
newPage(*myImage.size())
# draw the image
image(myImage, (0, 0))

saveImage('filterFun.png')