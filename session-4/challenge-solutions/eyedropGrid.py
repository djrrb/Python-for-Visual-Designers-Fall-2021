# define the image object
myImage = ImageObject('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/1920px-Juvenile_Ragdoll.jpg')

newPage(*myImage.size())

# draw a background
fill(0)
rect(0, 0, width(), height())

# how to make the grid
myRows = 50
myCols = 50

# calculate the size of each cell
myColWidth = width()/myCols
myRowHeight = height()/myRows



for myRow in range(myRows):
    # myRow = 0, 1, 2, 3...
    for myCol in range(myCols):
        # myCol = 0, 1, 2, 3...
        
        # calculate X and Y by multiplying column number by column width, and row number by row height
        myX = myCol * myColWidth
        myY = myRow * myRowHeight
        
        # eye drop the image at that X and Y
        myColor = imagePixelColor(myImage, (myX, myY))
        
        # set the fill to that color
        fill(*myColor)
        
        # draw a shape
        oval(myX, myY, myColWidth, myRowHeight)
        
saveImage('eyedropGrid.png')
