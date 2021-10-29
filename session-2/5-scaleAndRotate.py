# make a rotating scaling shape

# make background
rect(0, 0, width(), height())

# move the canvas by half width and height
# this means we draw from the center
translate(width()/2, height()/2)

# set a size variable
mySize = 800

# set stroke and fill
stroke(1, 0, 0)
strokeWidth(10)
fill(None) # make transparent

for myRectangle in range(50):
    print('this is my rectangle', myRectangle)
    # draw a rectangle
    # subtracting half width and height of object for x and y
    rect(-mySize/2, -mySize/2, mySize, mySize)
    # every time we draw a rectangle
    # also apply additional canvas transformations such as scale or rotate
    # these will add up over time
    scale(.90)
    rotate(6)
    # could translate and skew if we wanted
    #translate(50, 50)
    #skew(8)