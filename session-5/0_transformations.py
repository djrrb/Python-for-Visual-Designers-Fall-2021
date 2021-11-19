# move to center of canvas
translate(width()/2, height()/2)
# (0, 0) is pivot point
# rotate 45° around pivot point
rotate(45)

# draw blue square with pivot point in middle
fill(0, 1, 1)
rect(-50, -50, 100, 100)

# plot (0, 0)
fill(0)
oval(-10, -10, 20, 20)
text('0, 0', (20, 0))
# plot (100, 100)
oval(100-10, 100-10, 20, 20)
text('100, 100', (20+100, 0+100))
