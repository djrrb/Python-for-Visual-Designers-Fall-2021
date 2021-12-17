myFrames = 30

myFontPath = '../assets/CondorVariable-VF.ttf'

minWght = 200
maxWght = 900
wghtRange = maxWght - minWght
print(wghtRange)

for myFrame in range(myFrames):
    newPage()
    font(myFontPath, 800)
    with savedState():
        translate(0, height()/2)
        x = 0
        y = 0
        for myPhase in range(myFrames):
            yMultiplier = sin(pi*myPhase/myFrames)
            y = yMultiplier*height()/2
            print(y)
            if myPhase == myFrame:
                fill(1, 0, 0)
                oval(x-40, y-40, 80, 80)
                wghtValue = yMultiplier * wghtRange + minWght
                italValue = yMultiplier
            else:
                fill(0)
                oval(x-20, y-20, 40, 40)
            x += width()/myFrames
        
        
    fontVariations(wght=wghtValue, ital=italValue)
    fill(0, 0, 1)
    text('a', (width()/2, 300), align="center")

saveImage('variableFontAnimation.gif')