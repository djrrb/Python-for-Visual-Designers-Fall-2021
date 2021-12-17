myFrames = 10

# loop through each frame
for myFrame in range(myFrames):
    # draw a new page
    newPage()
    # move to the vertical center of the canvas
    translate(0, height()/2)
    # myFrame/myFrames is the progress of our animation between 0 and 1
    # width()*progress will make our dot move a little bit further each frame
    translate(width()*myFrame/myFrames)
    # draw a dot
    oval(-20, -20, 40, 40)

# save a gif
saveImage('simpleAnimation.gif')