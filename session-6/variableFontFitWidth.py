def norm(value, start, stop):
    """
    Map a value between 0 and 1 and return the corresponding position between start and stop
    https://p5js.org/reference/#/p5/norm
    """
    return start + (stop-start) * value

def lerp(start, stop, amt):
    """
    Map a value between start and stop and return the corresponding position between 0 and 1
    https://p5js.org/reference/#/p5/lerp
    """
    return float(amt-start) / float(stop-start)

myFontPath = '../assets/CondorVariable-VF.ttf'

myString = 'banan'

for myFrame in range(1):
    newPage()
    font(myFontPath, 200)
    print(listFontVariations())
    minWidthValue = listFontVariations()['wdth']['minValue']
    print(minWidthValue)
    fontVariations(wght=400, wdth=minWidthValue, ital=-.1)
    minWidth = textSize(myString)[0]
    maxWidthValue = listFontVariations()['wdth']['maxValue']
    fontVariations(wght=400, wdth=maxWidthValue, ital=-.1)
    maxWidth = textSize(myString)[0]
    print(minWidth, maxWidth)
    #text(myString, (0, 0))
    progress = lerp(minWidth, maxWidth, width())
    print(progress)
    valueIWant = norm(progress, minWidthValue, maxWidthValue)
    fontVariations(wght=400, wdth=valueIWant, ital=-.1)
    text(myString, (0, 0))
    
#saveImage('variableFontDemo.gif')