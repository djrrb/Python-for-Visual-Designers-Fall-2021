# set number of frames
myFrames = 30

# loop through frames
for myFrame in range(myFrames):
    newPage()
    # draw a background
    fill(1)
    rect(0, 0, width(), height())
    # move to vertical center of page
    translate(0, height()/2)
    
    # set a starting value for x
    x = 0
    # loop again to draw the result for each frame on each frame
    for myPhase in range(myFrames):
        # change our multiplier
        # 2*pi = full circle (up and down)
        # myPhase/myFrames = our progress through the cycle
        yMultiplier = sin(2*pi*myPhase/myFrames)
        # multiply that by half the height of the page
        # half because the numbers goes up and down
        y = yMultiplier*height()/2
        # if our phase is equal to our frame, draw a big red circle
        if myPhase == myFrame:
            fill(1, 0, 0)
            oval(x-40, y-40, 80, 80)
        else:
            # otherwise draw a smaller black circle
            fill(0)
            oval(x-20, y-20, 40, 40)
        # increase x every time
        x += width()/myFrames

# save results
saveImage('sineAnimation.gif')