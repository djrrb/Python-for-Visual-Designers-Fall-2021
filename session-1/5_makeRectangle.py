# draw a rectangle on a page
inch = 72

# make a new page, or give it an width, height sequence
#newPage('Letter')
newPage(8.5*inch, 11*inch)



# draw a rectangle, which takes 4 arguments:
# x, y, width, height
# by default it will be black
# 0, 0 is the bottom left corner
rect(0, 0, 100, 100)