# make an image object
myImage = ImageObject()

# everything below this will be drawn into my image
with myImage:
    # draw a bunch of shapes into the image
    for myNumber in range(100):
        fill(random(), random(), random())
        oval(random()*width(), random()*height(), 100, 100)
        
# blur the image
myImage.gaussianBlur()

# draw it to canvas
image(myImage, (0, 0))