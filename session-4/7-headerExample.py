# a practical savedState example

# set a margin variable
myMargin = 50

# make a function to draw a header
def myHeader():
    # save the state
    # this means the function is non-destructive and won’t influence things outside of it
    with savedState():
        # move to the top left
        translate(myMargin, height()-myMargin)
        # draw the header in red text
        fontSize(25)
        fill(1, 0, 0)
        text('this is the header',  (0, 0))
        
# make a page
newPage()
# draw the header
myHeader()
# do some content
# because of the savedState() in myHeader, the content will be drawn from the lower left 
rect(0, 0, 300, 300)

# showing how myHeader() can be reused
# always drawing from the lower left and moving to the upper right and then back again
newPage()
for myNumber in range(20):
    myHeader()
    translate(0, -20)