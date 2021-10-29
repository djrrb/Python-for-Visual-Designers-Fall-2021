myRect = 500
fill(0, 1, 0)

fontSize(100)
text('hello world', (800, 100))

with savedState():
    translate(width()/2, height()/2)
    fill(1, 0, 0)
    rect(-myRect/2, -myRect/2, myRect, myRect)
    fill(1)
oval(0, 0, 50, 50)