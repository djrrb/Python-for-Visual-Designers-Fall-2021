myFrames = 10

for myFrame in range(myFrames):
    newPage()
    # draw a background
    fill(1)
    rect(0, 0, width(), height())
    # move to vertical center
    translate(0, height()/2)
    # set default values for x and y
    x = 0
    y = 0
    # draw each dot on each frame, so make another loop
    for myPhase in range(myFrames):
        # if our phase is equal to our frame, draw a big red circle
        if myPhase == myFrame:
            fill(1, 0, 0)
            oval(x-40, y-40, 80, 80)
        else:
            # otherwise draw a smaller black circle
            fill(0)
            oval(x-20, y-20, 40, 40)
            
        # increase x each time
        x += width()/myFrames

# save gif
saveImage('complexAnimation.gif')