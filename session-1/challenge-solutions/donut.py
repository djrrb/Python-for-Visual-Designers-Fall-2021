# make a donut
# draw an big circle on the outside, make it black

thickness = 200

fill(0)
oval(0, 0, width(), height())
# draw a smaller white circle 
fill(1)
oval(thickness, thickness, width()-thickness*2, height()-thickness*2)