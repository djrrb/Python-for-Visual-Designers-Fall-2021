frames = 10

for frame in range(frames):
    newPage()
    frameDuration(.3)

    fontSize(100)
    rect(0, 0, width(), height())
    fill(None)
    stroke(0, 1, 0)
    strokeWidth(2)
    font('Impact')

    for repeat in range(100):
        x = random()*width()
        y = random()*height()
        text(str(frame), (x, y))
        
saveImage('randomNumbers.gif')