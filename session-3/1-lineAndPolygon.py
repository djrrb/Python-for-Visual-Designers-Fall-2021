# make a red stroke
strokeWidth(10)
stroke(1, 0, 0)

# draw a line
# it is a sequence of two (x, y) coordinates
line(
    (60, 50), # x, y
    (160, 500) # x, y
    )

# make a grey shape
stroke(None)
fill(.5)
    
# draw a polygon
# it is a squence of as many coordinates as you want points on the shape
polygon(
    (60, 50),
    (200, 200),
    (300, 800),
    (1000, 1000),
    (500, 20)
    )
