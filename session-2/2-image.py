
# draw an image a bunch of times!
for number in range(10):
    
    # use the image function
    # image(path, (x, y))
    image(
        'samplePdfFromIllustrator.pdf', 
        ( # this is the start of a tuple
            random()*width(),  #x 
            random()*height()  #y
        ) # this is the end of a tuple
    )