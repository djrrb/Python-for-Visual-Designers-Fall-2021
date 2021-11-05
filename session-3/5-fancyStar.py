from colorsys import hsv_to_rgb

myHandle = 340

# copy paste this from 
# https://forum.drawbot.com/topic/135/changing-squares-to-five-point-stars-with-jvr-code/4?_=1636078308228&lang=en-US
def star(x, y, n, r1, r2):
    # x = center x
    # y = center y
    # n = number of points
    # r1 = radius of outer points
    # r2 = radius of inner poitns
    pts = []
    for i in range(n * 2):
        a = i * pi / n
        r = r2 if i % 2 else r1
        pts.append((x + r * sin(a), y + r * cos(a)))
    polygon(*pts)

# set some variables
myWidth = 1000
myHeight = height()

# hue saturation value defaults
myHue = 0
mySat = 1
myVal = 1 

myStripeCount = 40 # how many shapes to draw

# make a stripe for each number in stripe count
for myStripe in range(myStripeCount):
    # convert hsv to rgb
    print(hsv_to_rgb(myHue, mySat, myVal))
    # set that to fill
    fill(*hsv_to_rgb(myHue, mySat, myVal))
    # draw a 5 pointed star
    star(width()/2, height()/2, 5, myWidth, myHeight)
    # each time, make my height a little smaller
    myHeight -= height()/myStripeCount
    
    # also augment the hue each time so we cycle through the rainbow
    myHue += 0.1
    
