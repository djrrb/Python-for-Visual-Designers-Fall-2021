# make an animation with rotating concentric squares

# first set some variables

# number of pages/frames
myPages = 60
# make my pages 360 to get a full rotation
#myPages = 360

# starting rotation, will increase on each page
myRotation = 0

# frames per second
fps = 12

# loop through a series of pages
for myPage in range(myPages):
    # myPage = 0, 1, 2, 3...
    print('this is page', myPage+1)
    
    # make the new page and set frame duration
    newPage()
    frameDuration(1/fps)

    # make background by filling the canvas with a rectangle
    rect(0, 0, width(), height())

    # move the canvas by half width and height
    # this means we will draw from the middle
    translate(width()/2, height()/2)

    # set a size variable
    mySize = width()

    # set stroke if we want
    stroke(0, 0, 0)
    strokeWidth(3)

    # draw a bunch of rectangles
    for myRectangle in range(40):
        # myRectangle = 0, 1, 2, 3...
        print('\tthis is my rectangle', myRectangle)

        # make a different color for odd and even
        # we can do this a couple different ways
        
        # test if the number divied by 2 is the same as an integer
        #print(myRectangle / 2, int(myRectangle / 2))
        #if myRectangle / 2 == int(myRectangle / 2):

        # or use the modulo (%) to get the remainder
        # this will alternate 0, 1, 0, 1, 0, 1
        
        # use an "if" statement to run code conditionally
        if myRectangle % 2:
            # if it’s odd, there is a remainder and we fill it green
            fill(0, 1, 0)
        else:
            # if it’s even, there’s no remainder and we fill it blue
            fill(0, 0, 1)
           
        # draw a rectangle
        # subtracting half width and height of object for x and y
 
        rect(-mySize/2, -mySize/2, mySize, mySize)
        scale(.9)
        # also move the canvas
        #translate(50, 50)
        # rotate by the number of degrees
        rotate(myRotation)
    
    # dedent, this will run once per page
    # at the end of each page, make it rotate a bit more
    # determine this bit by dividing 360 (a full rotation) by the number of frames
    # this way it will always do a full rotation in however many frames
    myRotation = myRotation + 360/myPages


print('done')

# save the file as a gif
saveImage('rotation.gif')