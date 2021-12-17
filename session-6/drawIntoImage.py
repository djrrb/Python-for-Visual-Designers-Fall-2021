myImage = ImageObject()

with myImage:
    for myNumber in range(100):
        fill(random(), random(), random())
        oval(random()*width(), random()*height(), 100, 100)
        
myImage.gaussianBlur()
image(myImage, (0, 0))