# define a drawLogo function. it takes a size argument that it uses to draw the logo
def drawLogo(myLogoSize):
    # make a geometric D out of a square and a circle
    # or something...
    rect(0, 0, myLogoSize/2, myLogoSize)
    oval(0, 0, myLogoSize, myLogoSize)

# set a multiplier for inches
inch = 72

myCardWidth = 3.5*inch
myCardHeight = 2*inch

# set some variables
myMargin = 20 # this does double duty as edge margin and margin between elements
myMarginWidth = myCardWidth-myMargin*2 # with of content
myMarginHeight = myCardHeight-myMargin*2
myLogoSize = 64 # arbitrary number determining size of logo
spotColor = 1, .2, .4
myFontSize = 10
myLeading = 1.6

# define a formatted string for the name
# include tracking and other stuff
myName = FormattedString(
    'David Jonathan Ross'.upper(), 
    font='Roslindale-TextRegular', 
    fontSize=myFontSize,
    tracking=2,
    )

# define a formatted string for the address
# use a multiline string with three quotes
myAddress = FormattedString(
    """P.O. Box 461
Conway, MA 01341 USA
""", 
    font='Roslindale-TextRegular', 
    fontSize=myFontSize,
    lineHeight=myFontSize*myLeading,
    )
# append web addresses in a separate font style
# you don’t have to redefine size, it will inherit anything you don't change
myAddress.append(
    """david@djr.com
@djrrb
    """,
    font='Roslindale-TextItalic'
    )


# now we have all the ingredients so let's make the card

def drawCard():
    # save the state of the card so that it doesn't transform the state of anything else outside of it
    with savedState():
        # move from the lower left to the lower left margin
        translate(myMargin, myMargin)

        # draw my name in the upper left
        # i am just lazily setting the box height manually to make it look good
        # i could calculate this if i wanted to
        textBox(myName, (0, 0, myMarginWidth, myMarginHeight))    
        # for the adress, shift it over by the width of the logo and then some
        # then draw the text box at the same height as the logo
        textBox(myAddress, (myLogoSize+myMargin, 0, myMarginWidth-myLogoSize, myLogoSize))

        # use the spot color, draw the logo 
        fill(*spotColor)
        drawLogo(myLogoSize)

        # now draw a line underneath the name to match
        stroke(*spotColor)
        strokeWidth(6)
        line((0, myLogoSize+myMargin), (myMarginWidth, myLogoSize+myMargin))


# Now make a sheet of cards

# make a new page
newPage(8.5*inch, 11*inch)

# set some variables for the page
mySheetMargin = 35
rows = 5
cols = 2

# move to the lower left
translate(mySheetMargin, mySheetMargin)

# loop through rows
for row in range(rows):
    # save our state so we can go back to the beginning of each row
    with savedState():
        # loop through cols
        for col in range(cols):
            # draw a faint border around each card
            with savedState():
                stroke(0, 0, 0, .1)
                fill(None)
                rect(0, 0, myCardWidth, myCardHeight)
            # draw the card
            drawCard()
            # move us over one column
            translate(myCardWidth, 0)
    # move us over one height
    translate(0, myCardHeight)

saveImage('businessCard-sheet.pdf')