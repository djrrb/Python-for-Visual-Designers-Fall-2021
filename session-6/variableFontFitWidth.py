# some functions
# see https://github.com/typemytype/drawbot/issues/414
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

# relative path to variable font
myFontPath = '../assets/CondorVariable-VF.ttf'

# the words we will loop through to fit to our canvas
words = ['the', 'quick', 'gray', 'fox']

myString = ''
# loop through words
for word in words:
    # add new word to sentence to make strings of different lengths
    myString += word 
    # make new page
    newPage(1000, 200)
    # set the font
    font(myFontPath, 200)
    # list of variable axes within the font
    print(listFontVariations())
    
    # ok let’s find the narrowest possible setting
    minWidthValue = listFontVariations()['wdth']['minValue']
    # set the font to the narrowest
    fontVariations(wght=400, wdth=minWidthValue)
    # now get the width of the text with those settings
    minWidth = textSize(myString)[0]
    
    # now get the widest possible setting
    maxWidthValue = listFontVariations()['wdth']['maxValue']
    # set the font to the maximum
    fontVariations(wght=400, wdth=maxWidthValue)
    # now get the width of the text with those settings
    maxWidth = textSize(myString)[0]
    
    # get a number between 0 and 1 that represents where we want to be on
    # the spectrum between minWidth and maxWidth
    progress = lerp(minWidth, maxWidth, width())
    
    # so the axis value I want to use is .XX between 0 (min) and 1 (max)
    valueIWant = norm(progress, minWidthValue, maxWidthValue)
    print(myString, progress, valueIWant)
    
    # set the current font variations with the axis value I want
    fontVariations(wght=400, wdth=valueIWant)
    # now draw the text
    text(myString, (0, -fontDescender()))
    # add a space to the string afterwards
    myString += ' '
    
#saveImage('variableFontDemo.gif')