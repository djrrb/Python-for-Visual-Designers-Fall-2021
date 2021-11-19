
newPage('Letter')

margin = 90
contentWidth = width()-margin*2
contentHeight = height()-margin*2
with savedState():
    fill(0, 0, 0, .1)
    rect(margin, margin, contentWidth, contentHeight)
        
        


myString = 'INVOICE'
        
myFormattedString = FormattedString(myString, fontSize=1, font='Comic Sans MS', lineHeight=1)

myTextWidth, myTextHeight = textSize(myFormattedString)

myFontSizeMultiplier = contentWidth / myTextWidth
print(myFontSizeMultiplier)
myFormattedString = FormattedString(myString, fontSize=myFontSizeMultiplier, font='Comic Sans MS')


print(myTextWidth, myTextHeight)

text(myFormattedString, (margin, contentHeight))
        
        