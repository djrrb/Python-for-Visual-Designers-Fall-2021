# draw a shape with straight lines on the sides and bottom, and a curve on the top

# import our hsv to rgb converter
from colorsys import hsv_to_rgb

myHandle = 100 # defualt handle length

def myShape(x, y, w, h):
    # make a new bezier path
    # we will define it first
    # draw it to canvas later
    myPath = BezierPath()
    # move to the lower left
    myPath.moveTo((x, y))
    # draw a line to the lower right
    myPath.lineTo((x+w, y))
    # draw a line up
    myPath.lineTo((x+w, y+h))
    # add or subtract some randomness from the shape
    myWobble = randint(-100, 100)
    # draw a curve back to the left
    # with two handles and an endpoint
    myPath.curveTo(
        ((x+w, y+h+myHandle+myWobble)), # handle 1
        ((x, y+h+myHandle+myWobble)), # handle 2
        ((x, y+h))# endpoint
        )
    drawPath(myPath)

# by default all stripes will go the full width of the canvas
myWidth = width()
# the first stripe will be drawn the full height of the canvas
myHeight = height()

# defaults for HSV, we will augment one of these
myHue = 0
mySat = 1
myVal = 1

# how many stripes to draw
myStripeCount = 21

# loop through each stripe
for myStripe in range(myStripeCount):
    
    # convert hsv to rgb using the function
    print(hsv_to_rgb(myHue, mySat, myVal))
    # use * to unpack it!
    fill(*hsv_to_rgb(myHue, mySat, myVal), .6)
    
    # draw the shape ad the determined width and height
    myShape(0, 0, myWidth, myHeight)
    
    # each time, make myHeight a litle shorter
    # subtract it by 1/x of the canvas
    # where x is equal to the stripe height
    myHeight -= height()/myStripeCount
    
    # augment hue to cycle through rainbow
    myHue += 0.1
    
