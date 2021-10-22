newPage('Letter')

# center a rectangle

# define a width and height for our rectangle
w = 100
h = 100

# determine the position
# get the x offset by taking the full width, subtracting the with of the object, dividing by two
x = (width()-w)/2
# do the same for height
y = (height()-h)/2
print(x, y)

# draw the rectangle
rect(x, y, w, h)