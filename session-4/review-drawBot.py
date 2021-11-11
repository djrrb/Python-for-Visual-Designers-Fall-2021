# A quick review of drawbot concepts.
"""
# SHAPE
rect()
oval()
polygon()
line()
Higher-level object: BezierPath()

# TEXT
text()
textBox()
Higher-level object: FormattedString()

# IMAGE
image()
imagePixelColor()
Higher-level object: ImageObject()

# CANVAS
translate()
scale()
rotate()
skew()
fill()
stroke()
width()
height()
clipPath()
"""

# %%%%%%%%%%%%%%%%%%%%%%%%% #
# %%%%    S H A P E    %%%% #
# %%%%%%%%%%%%%%%%%%%%%%%%% #

##############################
# rect(x, y, width, height)
##############################
newPage()
rect(200, 200, 600, 600)

##############################
# oval(x, y, width, height)
##############################
newPage()
oval(200, 200, 600, 600)

##############################
# polygon((x, y), (x2, y2)...)
##############################
newPage()
polygon(
    (random()*width(), random()*height()),
    (random()*width(), random()*height()),
    (random()*width(), random()*height()),
    (random()*width(), random()*height())
    )

##############################
# line((x, y), (x2, y2))
##############################
newPage()
stroke(0)
strokeWidth(20)
line((0, 0), (width(), height()))

##############################
# BezierPath()
# a higher level object for drawing paths
# create an instance of it
# do stuff to it (plot points, add text or shapes)
# draw it to the canvas
##############################
newPage()
# create a path instance
myPath = BezierPath()
# move to certain coordinates
myPath.moveTo((200, 200))
# draw a straight segment
myPath.lineTo((800, 200))
# draw another straight segment
myPath.lineTo((800, 800))
# draw a curved segment
myPath.curveTo(
        (500, 800), # first handle
        (200, 500), # second handle
        (200, 200) # point at end of segment
    )
# draw the object to the canvas
drawPath(myPath)


# %%%%%%%%%%%%%%%%%%%%%%%%% #
# %%%%    T  E  X  T    %%% #
# %%%%%%%%%%%%%%%%%%%%%%%%% #


##############################
# text(textString, (x, y))
##############################
newPage()
fontSize(100)
text('hello world', 
    (width()/2, height()/2),
    align="center"
    )

##############################
# textBox(textString, (x, y, w, h))
# (x, y, w, h) sequence is the same as rect()
##############################
newPage()
fontSize(100)
textBox(
    'The quick brown fox jumps over the lazy dog.', 
    (200, 200, 600, 600)
    )
    
##############################
# FormattedString()
# A higher level object for text that carries its own formatting.
##############################
newPage()
# create a formatted string instance
myString = FormattedString(
    'The quick brown fox', 
    font='Georgia', 
    fontSize=100
    )
# add to it, and change some formatting
myString.append(
    ' jumps over the lazy dog.', 
    fill=(0, 1, .5), 
    tracking=0, 
    font='Comic Sans MS', 
    fontSize=75
    )
# draw it to the canvas
textBox(
    myString, 
    (200, 200, 600, 600)
    )
    
    
# %%%%%%%%%%%%%%%%%%%%%%%%% #
# %%%%    I M A G E    %%%% #
# %%%%%%%%%%%%%%%%%%%%%%%%% #

##############################
# image(imagePath, (x, y))
##############################
newPage()
image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg', (0, 0))

##############################
# ImageObject(imagePath)
# a higher level object for storing images
# - query its size with the size method
# - draw it to canvas
##############################
newPage()
# - create an instance
myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')
# add filters or modify
myImage.sepiaTone()
myImage.bloom(20)
# scale so the width of the image fits in the canvas
scale(width()/myImage.size()[0])
# draw the image to canvas
image(myImage, (0, 0))

##############################
# imagePixelColor(imagePath, (x, y))
##############################
newPage()
myColor = imagePixelColor(myImage, (50, 50))
fill(*myColor)
rect(0, 0, width(), height())



# %%%%%%%%%%%%%%%%%%%%%%%%% #
# %%%    C A N V A S    %%% #
# %%%%%%%%%%%%%%%%%%%%%%%%% #

##############################
# translate(x, y)
##############################
newPage()
translate(width()/2, height()/2)
rect(0, 0, 200, 200)
rect(0, 0, -200, -200)

##############################
# rotate(degrees)
##############################
newPage()
translate(width()/2, height()/2)
rotate(45)
rect(0, 0, 200, 200)
rect(0, 0, -200, -200)

##############################
# scale(multiplier, yMultiplier)
##############################
newPage()
translate(width()/2, height()/2)
scale(2)
rect(0, 0, 200, 200)
rect(0, 0, -200, -200)

##############################
# skew(degrees)
##############################
newPage()
translate(width()/2, height()/2)
skew(20)
rect(0, 0, 200, 200)
rect(0, 0, -200, -200)

##############################
# fill(red, green, blue [, alpha])
# cmykFill(c, m, y, k, alpha) also exists
##############################
newPage()
fill(1, 0, 0)
rect(200, 200, 600, 600)

##############################
# stroke(red, green, blue [, alpha])
# cmykStroke(c, m, y, k, alpha) also exists
##############################
newPage()
stroke(1, 0, 0)
strokeWidth(20)
fill(None)
rect(200, 200, 600, 600)

##############################
# width() and height()
# get the width and height of 
# the current canvas
##############################
newPage()
rect(0, 0, width(), height())

##############################
# savedState()
# save your spot
# this way, when you add formatting you can also determine where that formatting ends
##############################
newPage()
# draw text in Red Georgia
font('Georgia', 100)
fill(1, 0, 0)
text('text #1', (200, 800))
with savedState():
    # change the font to blue comic sans 
    # for all things set at this indent
    font('Comic Sans MS')
    fill(0, 0, 1)
    text('text #2', (200, 650))
    with savedState():
        # add a stroke to all things set at this indent
        stroke(0, 1, 0)
        strokeWidth(5)
        text('text #3', (200, 500))
    # dedent once
    text('text #4', (200, 350))
# back to original formatting
text('text #5', (200, 200))

##############################
# clipPath()
##############################
newPage()
# make a path
myPath = BezierPath()
myPath.moveTo((200, 200))
myPath.lineTo((800, 200))
myPath.lineTo((800, 800))
myPath.curveTo(
        (500, 800),
        (200, 500),
        (200, 200)
    )
# create a saved state
with savedState():
    # clip everything within the state
    clipPath(myPath)
    # draw an image
    image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg', (-200, -450))
