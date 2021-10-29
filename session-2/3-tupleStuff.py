# set some x and y coordinates
coordinates = (200, 600)

# set up seme r,g,b
# you don’t need the parens to make a tuple
# it’s nice because we don’t have to manage red, green, blue separately 
fgColor = .5, 0, 1
bgColor = 0, .5, 0

# print the coordinates
print(coordinates)
# print only the first item in the tuple
print(coordinates[0])
# print only the second item in the tuple
print(coordinates[1])

# fill() takes r, g, b as three separate arguments
# use * to “unpack” the tuple and feed each item as a separate argument
fill(*bgColor)
rect(0, 0, width(), height())

# draw a foreground shape
fill(*fgColor)
rect(100, 200, 500, 500)

# now do something different
fill(1, 1, 0)
fontSize(30)
text('this is yellow text just to do something different', (20, 20))

# and now it’s easy to reapply our foreground color
fill(*fgColor)
oval(180, 800, 500, 500)