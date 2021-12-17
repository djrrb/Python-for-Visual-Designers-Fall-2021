myFontPath = '../assets/CondorVariable-VF.ttf'

myWght = 200
for myFrame in range(10):
    newPage()
    font(myFontPath, 200)
    fontVariations(wght=myWght, wdth=150, ital=-.1)
    text('hello world', (0, 0))
    myWght += 100
    
saveImage('variableFontDemo.gif')