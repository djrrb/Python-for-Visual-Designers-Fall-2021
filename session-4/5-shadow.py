# draw a shadow
shadow(
    (-50, -50), # offset
    50, # blur
    (1, 0, 0) # color
)

# it will now apply to anything after it
rect(100, 100, 500, 500)
fontSize(200)
text('hello world', (200, 800))