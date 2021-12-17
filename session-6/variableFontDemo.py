# relative path
myFontPath = '../assets/CondorVariable-VF.ttf'

# set a starting weight
myWght = 200
# loop through some frames
for myFrame in range(10):
    # make a new page
    newPage(1000, 200)
    # make background
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    # set the font
    font(myFontPath, 200)
    # 
    fontVariations(
        wght=myWght, # the weight 
        wdth=150, # the width
        ital=.5 # the italic value
        )
    # draw the text to canvas
    # vertically offset by the font's descender
    text('hello world', (0, -fontDescender()))
    # each time, increase the weight value to make it heavier
    myWght += 80

# save as gif
saveImage('variableFontDemo.gif')