# define a triangle function
def triangle(x, y, w, h):
    # inside this function, the arguments x,y,w,h exist
    print('this is a triangle', x, y, w, h)
    # use polygon to draw the triangle
    polygon(
        (x, y), # lower left corner
        (x+w/2, y+h), # half way across, all the way up
        (x+w, y) # all the way across, back down
        )
    
# make a bunch of triangles
for myNumber in range(100):
    # get a random x and y coordinate
    triX = randint(0, width())
    triY = randint(0, height())
    # fill with a random color, make it semitransparent
    fill(random(), random(), random(), .1)
    # call the triangle() function to draw the shape
    triangle(triX, triY, 200, 200)

# draw an extra triangle, just because we can
fill(1, 0, 0)
triangle(0, 0, 100, 100)