# okay this is a complicated one!

# import hsv to rgb conversion
from colorsys import hsv_to_rgb

# define a shape
# this will draw a single stripe with a curve on top
def myShape(x, y, w, h):
    myHandle = 340
    #rect(x, y, w, h)
    myPath = BezierPath()
    myPath.moveTo((x, y))
    myPath.lineTo((x+w, y))
    myPath.lineTo((x+w, y+h))
    myWobble = randint(-500, 500)
    myPath.curveTo(
        ((x+w, y+h+myHandle+myWobble)), # handle 1
        ((x, y+h-myHandle+myWobble)), # handle 2
        ((x, y+h))# endpoint
        )
    drawPath(myPath)

# define a background
# this will draw a bunch of shapes, messing with values
def background():
    # set defaults for HSV
    myHue = .3
    mySat = .4
    myVal = .5
    # set width and height for stripe
    myWidth = 1000
    myHeight = height()

    # determine how many stripes
    myStripeCount = 21

    # draw each stripe in a loop
    for myStripe in range(myStripeCount):
        # set the color, unpacking the RGB tuple result
        print(hsv_to_rgb(myHue, mySat, myVal))
        fill(*hsv_to_rgb(myHue, mySat, myVal), .5)
        # draw the shape
        myShape(0, 0, myWidth, myHeight)
        
        # now do our transformations for next time
        # augment the height so it’s a little smaller each time
        myHeight -= height()/myStripeCount
        # make the saturation random each time 
        mySat = random()
        # choose between .4 and .6 as a hue
        myHue = randint(4,6)/10
    

########
########
########
########

########
########
########
########
########
########
########
########

#####
# Now let’s prepare our text


# define a formatted string
# this text carries its formatting with it
myText = FormattedString('hello world ', fontSize=15)

# append some formattet text to it
myText.append('here is more text ', fill=(0, 1, 0))

# and some more with a different font
myText.append('here is more text', fill=(0, 1, 1), font='Georgia')

# loop through each of the first 1000 fonts and add it to myText
for fontName in installedFonts()[0:1000]:
    # skip it if it includes a period
    if '.' not in fontName:
        # append the font name
        # set in the font
        # and a random color
        myText.append(
            fontName+' ', 
            font=fontName, 
            fill=(random(), random(), random()))

######
######
######
######
######
######

# define a starting point for page numbers
myPageNum = 1

# Do a while loop
# this will run while a certain condition is true

# myText cotains all our text, but we will reset it every time to only contain the overflow
# we will whittle it down until it no longer contains anything
# at which point it will be false and the loop will stop
while myText:
    #make page
    newPage("Letter")

    # draw background
    background()

    # defining margins
    myMargin = 50
    # myMarginWidth/Height are equal to the size of the white box
    myMarginWidth = width()-myMargin*2
    myMarginHeight = height()-myMargin*2
    # myInnerMarginWidth/Height are equal to the size of the text block
    myInnerMarginWidth = myMarginWidth-myMargin*2
    myInnerMarginHeight = myMarginHeight-myMargin*2

    # draw white background
    translate(myMargin, myMargin)
    fill(1)
    rect(0, 0, myMarginWidth, myMarginHeight)

     #move to interior margin
    translate(myMargin, myMargin)
    stroke(None)
    # the textBlock returns the overflow text
    # myText turns into only the overflow
    myText = textBox(myText, (0, 0, myInnerMarginWidth, myInnerMarginHeight))
    fill(0)
    # draw footer as separate text, no box necesary
    text('Page '+str(myPageNum), (0, -10))
    
    # augment page number
    myPageNum += 1
    