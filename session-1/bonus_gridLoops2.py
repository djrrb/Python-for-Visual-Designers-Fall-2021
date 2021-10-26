cellSize = 20

newPage(1000, 1000)

x = 0
y = 0

for row in range(10):
    # row = 0, 1, 2, 3...
    for col in range(10):
        # col = 0, 1, 2, 3...
        #print(row, col)
        oval(x, y, cellSize, cellSize)
        x = x + cellSize
        # x += cellSize
    y = y + cellSize
    x = 0

###############
###############
###############

newPage()


for row in range(50):
    # row = 0, 1, 2, 3...
    fill(random(), random(), random())
    for col in range(50):
        # col = 0, 1, 2, 3...
        print(row, col)
        
        oval(col*cellSize, row*cellSize, cellSize, cellSize)