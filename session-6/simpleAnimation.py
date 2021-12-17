myFrames = 10

for myFrame in range(myFrames):
    newPage()
    translate(0, height()/2)
    translate(width()*myFrame/myFrames)
    oval(-20, -20, 40, 40)

saveImage('simpleAnimation.gif')