# set a number of frames
myFrames = 10
myShapeGroupCount = 20
myShapeCount = 10

# loop through each frame
for myFrame in range(myFrames):
    # make a new page
    newPage()
    frameDuration(.2)
    # make a background
    fill(0)
    rect(0, 0, width(), height())
    # we are going to draw a bunch of groups of concentric circles
    # first loop through the groups
    for shapeGroup in range(myShapeGroupCount):
        # place the group at a random width and height
        x = random()*width()
        y = random()*height()
        # each group will start at 100 units wide
        myShapeSize = 200
        # now draw each shape, centered at (x, y)
        for shape in range(myShapeCount):
            # make it a random color
            fill(random(), random(), random())
            # if the group is odd, make it a circle
            # if it’s even, make it a square

            if shapeGroup % 2:
                oval(
                    x-myShapeSize/2, # x
                    y-myShapeSize/2, # y
                    myShapeSize,  # width
                    myShapeSize # height
                )
            else:
                rect(
                    x-myShapeSize/2, # x
                    y-myShapeSize/2, # y
                    myShapeSize,  # width
                    myShapeSize # height
                )
                
            # each time I draw a shape
            # make it a little smaller
            # so you can see the bigger ones behind it
            myShapeSize = myShapeSize - 20
    
saveImage('concentricShapes.gif')