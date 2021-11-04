from colorsys import hsv_to_rgb

myHandle = 340

def star(x, y, n, r1, r2):
    pts = []
    for i in range(n * 2):
        a = i * pi / n
        r = r2 if i % 2 else r1
        pts.append((x + r * sin(a), y + r * cos(a)))
    polygon(*pts)



def myShape(x, y, w, h):
    #rect(x, y, w, h)
    myPath = BezierPath()
    myPath.moveTo((x, y))
    myPath.lineTo((x+w, y))
    myPath.lineTo((x+w, y+h))
    myWobble = randint(-100, 100)
    myPath.curveTo(
        ((x+w, y+h+myHandle+myWobble)), # handle 1
        ((x, y+h-myHandle+myWobble)), # handle 2
        ((x, y+h))# endpoint
        )
    drawPath(myPath)

myWidth = 1000
myHeight = height()

myHue = 0
mySat = 1
myVal = 1

myStripeCount = 21

for myStripe in range(myStripeCount):
    print(hsv_to_rgb(myHue, mySat, myVal))
    fill(*hsv_to_rgb(myHue, mySat, myVal))
    #myShape(0, 0, myWidth, myHeight)
    star(width()/2, height()/2, 5, myWidth, myHeight)
    myHeight -= height()/myStripeCount
    
    myHue += 0.1
    
