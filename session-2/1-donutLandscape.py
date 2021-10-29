# use a multiline string as a comment
"""this is an example
of a multiline string"""

#newPage("Letter")

newPage('LetterLandscape')

myDonutWidth = width()
myDonutHeight = height()
myDonutThickness = 230

oval(0, 0, myDonutWidth, myDonutHeight)

fill(1, 0, 0)
# oval(x, y, width, height)
oval(
    myDonutThickness,  # x
    myDonutThickness,  # y
    myDonutWidth-myDonutThickness*2, # width
    myDonutHeight-myDonutThickness*2) # height

# save it as donut.pdf in this same folder
saveImage('donut.pdf')