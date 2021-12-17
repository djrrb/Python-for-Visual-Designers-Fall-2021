myFrames = 10

for myFrame in range(myFrames):
    newPage()
    translate(0, height()/2)
    x = 0
    y = 0
    for myPhase in range(myFrames):
        if myPhase == myFrame:
            fill(1, 0, 0)
            oval(x-40, y-40, 80, 80)
        else:
            fill(0)
            oval(x-20, y-20, 40, 40)
        x += width()/myFrames

saveImage('simpleAnimation.gif')