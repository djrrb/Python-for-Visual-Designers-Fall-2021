# make a new page at a preset size
# https://drawbot.com/content/canvas/pages.html#drawBot.newPage
newPage('Letter')

# set the font
# font can be the menu name of a font as a string
# ( see all menu names using print(installedFonts()) )
# it can also be a path to a font on your computer
# '/myfolder/Font.otf'

font('Times New Roman Bold')
# set the font size
# numbers are in points
fontSize(100)
text('hello', (100, 100))
