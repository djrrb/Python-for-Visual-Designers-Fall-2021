# define a formatted string
myString = FormattedString('A', font='Comic Sans MS', fontSize=1000)

# define a bezier path
myPath = BezierPath()

# feed our formatted string to the bezier path
# this is like “create outlines” in illustrator
myPath.text(myString)

# we can draw the string as text
text(myString, (0, 0))
# we can draw the path as an outline
fill(1, 0, 0)
drawPath(myPath)

# we can also use the path as a clipping mask
# save the state first so that we can control what does and does not end up in the clip path
with savedState():
    # clip using our path that we've defined
    clipPath(myPath)
    # draw a bunch of stuff to be clipped
    for myShape in range(1000):
        fill(random(), random(), random())
        oval(random()*width(), random()*height(), 50, 50)
    
# draw something outside of the clipPath(), just to show that we're out of it now
oval(width(), height(), -50, -50)

# save the image
saveImage('clipPathText.pdf')