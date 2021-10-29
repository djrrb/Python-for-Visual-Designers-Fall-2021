# make background
rect(0, 0, width(), height())

# move the canvas by half width and height
translate(width()/2, height()/2)

# rect(x, y, width, height)
# set a size variable
mySize = width()

# set stroke
stroke(1, 0, 0)
strokeWidth(10)
# make transparent

# True, False are also things

for myNumber in range(20):
    fill(None)
    #print(myNumber)
    # draw a rectangle
    # subtracting half width and height of object for x and y
    rect(-mySize/2, -mySize/2, mySize, mySize)
    translate(50, 50)



