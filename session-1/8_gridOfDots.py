# make a new page
newPage(1000, 1000)

# set our x and y to 0
# we will redefine these variables
# to draw our shapes at different positions
x = 0
y = 0

# do a loop within a loop
for anotherLetter in 'helloworld':
    # code at this indent will run 10 times
    for letter in 'helloworld':
        # code at this indent will run 100 times
        print(letter)
        fill(random(), random(), random())
        oval(x, y, 100, 100)
        x = x + 100
    # dedent to exit the inner loop
    # at the end of each row that we draw
    # increase Y to draw higher on the page
    y = y + 100
    # also, move x back to 0
    x = 0

# dedent to exit the outer loop
print('done')

# save this to our desktop as a png
saveImage('~/desktop/grid.png')
