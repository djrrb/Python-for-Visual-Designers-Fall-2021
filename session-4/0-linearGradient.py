# set a gradient as the fill color
linearGradient(
    (100, 100),                         # startPoint
    (800, 100),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .5, 1]                          # locations
    )
# draw a rectangle
fontSize(200)
text('hello world', (0, 0))