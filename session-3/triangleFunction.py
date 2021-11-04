# strokeWidth(10)
# stroke(0)

# line(
#     (60, 50), # x, y
#     (160, 200) # x, y
#     )
    
# polygon(
#     (60, 50),
#     (200, 200),
#     (300, 800),
#     (1000, 1000),
#     (500, 20)
#     )

def triangle(x, y, w, h):
    print('this is a triangle', x, y, w, h)
    polygon(
        (x, y),
        (x+w/2, y+h),
        (x+w, y)
        )
fill(1, 0, 0)

for myNumber in range(100):
    triX = randint(0, width())
    triY = randint(0, height())
    fill(random(), random(), random(), .1)
    triangle(triX, triY, 200, 200)
    
fill(1, 0, 0)
triangle(0, 0, 100, 100)