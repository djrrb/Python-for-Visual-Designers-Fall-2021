# verb() = function
# variable = value
"""hello this is a 
asdflknsd
a;lsfna;sdlf
askndfopaiwegnas
asfasp
asdnopasdvz

asdfoi
stringy comment"""

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

# draw an image!
for number in range(10):
    image(
        'Untitled3.pdf', 
        ( # this is the start of a tuple
            random()*width(),  #x 
            random()*height()  #y
        ) # this is the end of a tuple
    )