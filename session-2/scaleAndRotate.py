myPages = 9
for myPage in range(myPages):
    print('this is page', myPage+1)
    newPage()

    # make background
    rect(0, 0, width(), height())

    # move the canvas by half width and height
    translate(width()/2, height()/2)

    # rect(x, y, width, height)
    # set a size variable
    mySize = width()

    # set stroke
    stroke(1, 0, 0)
    strokeWidth(10)
    # make transparent

    # True, False are also things


    for myRectangle in range(10):
        fill(None)
        print('\tthis is my rectangle', myRectangle)
        # draw a rectangle
        # subtracting half width and height of object for x and y
        rect(-mySize/2, -mySize/2, mySize, mySize)
        scale(.84)
        #translate(50, 50)
        rotate(18)


print('done')



