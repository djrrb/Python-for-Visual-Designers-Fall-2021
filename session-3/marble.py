from colorsys import hsv_to_rgb

def myShape(x, y, w, h):
    myHandle = 340
    #rect(x, y, w, h)
    myPath = BezierPath()
    myPath.moveTo((x, y))
    myPath.lineTo((x+w, y))
    myPath.lineTo((x+w, y+h))
    myWobble = randint(-500, 500)
    myPath.curveTo(
        ((x+w, y+h+myHandle+myWobble)), # handle 1
        ((x, y+h-myHandle+myWobble)), # handle 2
        ((x, y+h))# endpoint
        )
    drawPath(myPath)

def background():
    myHue = .3
    mySat = .4
    myVal = .5
    
    myWidth = 1000
    myHeight = height()


    myStripeCount = 21

    for myStripe in range(myStripeCount):
        print(hsv_to_rgb(myHue, mySat, myVal))
        fill(*hsv_to_rgb(myHue, mySat, myVal), .5)
        myShape(0, 0, myWidth, myHeight)
        #star(width()/2, height()/2, 5, myWidth, myHeight)
        myHeight -= height()/myStripeCount
    
        mySat = random()
        myHue = randint(4,6)/10
    

########
########
########
########

########
########
########
########
########
########
########
########

myText = FormattedString('hello world ', fontSize=15)

myText.append('here is more text ', fill=(0, 1, 0))

myText.append('here is more text', fill=(0, 1, 1), font='Georgia')


for fontName in installedFonts()[0:1000]:
    if '.' not in fontName:
        myText.append(fontName+' ', font=fontName, fill=(random(), random(), random()))

######
######
######
######
######
######

myPageNum = 1


while myText:
    #make page
    newPage("Letter")

    # draw background
    background()

    # defining margins
    myMargin = 50
    myMarginWidth = width()-myMargin*2
    myMarginHeight = height()-myMargin*2
    myInnerMarginWidth = myMarginWidth-myMargin*2
    myInnerMarginHeight = myMarginHeight-myMargin*2

    # draw white background
    translate(myMargin, myMargin)
    fill(1)
    rect(0, 0, myMarginWidth, myMarginHeight)

    # draw text box
    translate(myMargin, myMargin)
    stroke(None)
    myText = textBox(myText, (0, 0, myInnerMarginWidth, myInnerMarginHeight))
    fill(0)
    text('Page '+str(myPageNum), (0, -10))
    myPageNum += 1
    