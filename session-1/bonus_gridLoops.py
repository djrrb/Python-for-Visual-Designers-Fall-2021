# three different ways to make a grid with loops

# make some variables to control certain attribues
cellSize = 100
cols = 10
rows = 10

########################################
# approach one
# define x and y variables, then augment them
########################################
newPage(cellSize*cols, cellSize*rows)

x = 0
y = 0
for col in range(cols):
    # col = 0, 1, 2, 3...
    for row in range(rows):
        # row = 0, 1, 2, 3...
        fill(random(), random(), random())
        rect(x, y, cellSize, cellSize)
        # after drawing each column, move 100 to the right
        x = x + cellSize
    # after drawing each row, move 100 up
    y = y + cellSize
    # also reset x to 0, so that we return to the far left of the page
    x = 0
    
########################################
# approach 2
# multiply cell size by row/column index

# rather than defining x and y variables
# we determine x by multiplying the col index (0, 1, 2, 3) by the cellWidth
# and same for row index and height
########################################
newPage(cellSize*cols, cellSize*rows)
for col in range(cols):
    # col = 0, 1, 2, 3...
    for row in range(rows):
        # row = 0, 1, 2, 3...
        fill(random(), random(), random())
        rect(col*cellSize, row*cellSize, cellSize, cellSize)
        
########################################
# approach 3
# get the x and y values directly from the range() we are looping through
# range() has an optional step argument that will skip a certain amount between each number in our range
# if we skip each by 100, we will get 100, 200, 300, 400.

# (note this only works if our width, height, and cellSize are integers!)
########################################

newPage(cellSize*cols, cellSize*rows)
#        range(start, stop, step)
for x in range(0, width(), cellSize):
    # x = 0, 100, 200, 300, 400
    #        range(start, stop, step)
    for y in range(0, height(), cellSize):
        # y = 0, 100, 200, 300, 400
        fill(random(), random(), random())
        rect(x, y, cellSize, cellSize)