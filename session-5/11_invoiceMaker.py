################################
#########    PART 1    #########
######### GET THE DATA #########
################################

# import the CSV library
import csv

# which customer are we creating the invoice for
myCustomerNumber = 2

# make an empty dictionary
# we will populate it with customer info
customerData = {}

# open the CSV file and call it customerFile
with open('assets/customers.csv', encoding='utf-8') as customerFile:
    # use the csv reader to read it as a CSV
    customerReader = csv.reader(customerFile)
    # loop through each row, and create a variable for the index of the row
    for rowIndex, rowContent in enumerate(customerReader):
        # skip the first row
        # but save the header names as customerHeaders
        if rowIndex == 0:
            customerHeaders = rowContent
            continue
        # if the first column (the ID) is equal to the customer number
        # this is our match!
        if int(rowContent[0]) == myCustomerNumber:
            # loop through each cell and add it to the customer data
            # {'Name': 'My Name', 'Telephone': '555-5555'} etc
            for cellIndex, cellContent in enumerate(rowContent):
                # get the key from customerHeaders
                # get the value from cellContent
                # dict[key] = value
                customerData[customerHeaders[cellIndex]] = cellContent
            # we only want one customer, so after this we don’t need to loop anymore so we can break the loop
            break
           
# okay now find the projects that match this customer
# make an empty list that we will populate with projects
myProjects = [] 
# open the projects.csv
with open('assets/projects.csv', encoding='utf-8') as projectsFile:
    # read it as a csv reader object
    projectsReader = csv.reader(projectsFile)
    # loop through each row in that object
    for rowIndex, rowContent in enumerate(projectsReader):
        # skip the first row since it is headers
        if rowIndex == 0:
            continue
        # this time we only want to match rows where the customer number matches our customer number AND the row is unpaid 
        if int(rowContent[2]) == myCustomerNumber and rowContent[5] != 'TRUE':
            # we *could* add each row as a dictionary matching column header to row content. Or we can just append the row as a whole and access each cell by its column index
            myProjects.append(rowContent)
                            

######################################
#########       PART 2       #########
######### SET UP THE CONTENT #########
######################################

# ======= HELPER FUNCTIONS =======
# a cursor function to help us keep track of where we are
def cursor():
    with savedState():
        fill(1, 0, 0)
        oval(-10, -10, 20, 20)
            
# a mini function that uses .format() to quickly turn a number into a nicely formatted dollar sign
# more at https://www.python.org/dev/peps/pep-3101/
# https://www.kite.com/python/answers/how-to-format-currency-in-python
def formatCost(myNumber):
    return "${:,}". format(myNumber)

# a mini function that takes a string with a number in it and strips out $ and , and converts it to an integer
def costToInt(myCost):
    return int(myCost.replace('$', '').replace(',', ''))
            
            
# ======== BASIC VARIABLES =======
# make a new page
newPage('Letter')

# define some formatting variables
margin = 50
addressHeight = 96 # we could figure this out dynamically 
myTitleFont = 'Impact'
myContentFont = "Courier"
myContentBoldFont = 'Courier Bold'
myContentFontSize = 12.5 
myLineHeight = 1.5 # defining line heights as a multiplier so only relative to font size
myProjectLineHeight = 3 # projects get more space between them

# from these constants, figure out the content and column dimensions
contentWidth = width()-margin*2
contentHeight = height()-margin*2
columnWidth = (contentWidth-margin)/2

# what should the invoice title be
myTitleText = 'Invoice'.upper()

# ======= CONTACT INFO =======

# make a formatted string with my own contact info
# the first formatting block is bold and just contains my name
myContactInfo = FormattedString(
    'David Jonathan Ross', 
    font=myContentBoldFont, 
    fontSize=myContentFontSize, 
    lineHeight=myContentFontSize*myLineHeight
)
# after that, append my address and stuff, but make it not-bold
myContactInfo.append("""
P.O. Box 461
Conway, MA 01341
USA
david@djr.com
""", 
    font=myContentFont
)

# now do the same for their contact info
# instead of writing out the info explicitly we can query our customerData dictionary

theirContactInfo = FormattedString(
    customerData['Name'], 
    font=myContentBoldFont, 
    fontSize=myContentFontSize, 
    lineHeight=myContentFontSize*myLineHeight
)
# now add all their other information in the lighter weight
# separating them by new lines
theirContactInfo.append(
    '\n'+customerData['Address']+'\n'+customerData['E-mail'], 
    font=myContentFont
)

# now make two separate strings for project names and project costs
# just format them, but leave them empty for now
myProjectString = FormattedString('PROJECT\n',
    font=myContentBoldFont, 
    fontSize=myContentFontSize, 
    lineHeight=myContentFontSize*myProjectLineHeight)

myProjectCostString = FormattedString('COST\n',
    font=myContentBoldFont, 
    fontSize=myContentFontSize, 
    lineHeight=myContentFontSize*myProjectLineHeight)

# set a variable to keep track of the total cost
totalCost = 0

# loop through each project
for myProject in myProjects:
    # get the name from the second column
    myProjectName = myProject[1]
    # and the cost from the fifth column
    # use the helper function to convert it to an integer
    myProjectCost = costToInt(myProject[4])
    
    
    # append those to our project string and name strings using the regular font
    myProjectString.append(myProjectName+'\n', font=myContentFont)
    # use the helper function to convert our int back to a properly formatted dollar cost
    myProjectCostString.append(formatCost(myProjectCost)+'\n', font=myContentFont)
    
    # also add the project cost to the total cost
    totalCost += myProjectCost

# now set the total due, adding \n to skip a line
myProjectString.append('\nTOTAL DUE:', font=myContentBoldFont)
# also add the total cost, again using our helper function formatCost() to convert it to a nice pretty number
myProjectCostString.append('\n'+formatCost(myProjectCost), font=myContentBoldFont)


# Okay, now we’ve gathered the data
# And we’ve assembled it in FormattedStrings
# now it’s time to....
############################
#####      PART 3      #####
##### LAY OUT THE PAGE #####
############################

# move to the bottom left of the content space
translate(margin, margin)

# we want to be able to move back here, so save our state
with savedState():
    
    # if we want to visualize the content dimensions, we can draw it as a rect
    drawContentRect = False
    if drawContentRect:
        with savedState():
             fill(0, 0, 0, .1)
             rect(0, 0, contentWidth, contentHeight)

    # ============ DRAW THE TITLE! ============
    # since we want to size it dyamically, 
    # the first thing we do is make a formatted string
    # just to figure out its proportions
    myTitleStringTest = FormattedString(
        myTitleText, 
        font=myTitleFont, 
        fontSize=1, 
        lineHeight=1
    )
    # i use fontSize 1 so that the textSize width will tell me
    # how many times wider it is than it is tall
    myTitleWidth = textSize(myTitleStringTest)[0]
    # now that i know the proportion, I can divide that by the contentWidth to get the titleHeight, which is also the fontSize
    myTitleFontSize = contentWidth / myTitleWidth
    
    # NOW get a FormattedString using this font size
    myTitleString = FormattedString(myTitleText, font=myTitleFont, fontSize=myTitleFontSize)
    # we want to align the top to the cap height
    myCapHeight = myTitleString.fontCapHeight()
    
    # move up from the bottom left of the content height to the place where we will draw the title
    # this is the top left corner MINUS the cap height of the font
    translate(0, contentHeight-myCapHeight)
    
    # draw the title, woo!
    text(myTitleString, (0, 0))

    translate(0, -addressHeight-margin)

    # ============ DRAW THE ADDRESSES! ============
    
    # draw two text boxes, one on the left and one in the middle of the page
    
    # draw the first one with myContactInfo
    #rect(0, 0, columnWidth, addressHeight)
    textBox(myContactInfo, (0, 0, columnWidth, addressHeight))

    # since we know we are only moving to the right temporarily
    # save the state beforehand
    with savedState():
        translate(columnWidth+margin, 0)

        #rect(0, 0, columnWidth, addressHeight)
        textBox(theirContactInfo, (0, 0, columnWidth, addressHeight))
        
        # uncomment these cursors to see the effect of the saved states
        #cursor() # draws on the right column address height
    #cursor() # draws on the left column address height
#cursor() # back to the lower left corner of the content

# now figure out how tall we can make the box where we’re going to put the projects
myBoxHeight = contentHeight - myCapHeight - margin - addressHeight - margin

# draw the projects and costs columns
#rect(0, 0, contentWidth, myBoxHeight)
textBox(myProjectString, (0, 0, contentWidth, myBoxHeight))
textBox(myProjectCostString, (columnWidth+margin, 0, contentWidth, myBoxHeight))

# if we want to draw horizontal rules, we can do that in a saved state
with savedState():
    # move back up to the top of the box Height, and add a little to draw the line in the margin
    translate(0, myBoxHeight-myContentFontSize*myProjectLineHeight)
    # set the formatting for the rules
    stroke(0)
    strokeWidth(1)
    lineDash(2) # oh yeah we can do a dotted line!
    # draw the first line up top
    line((0, 0), (contentWidth, 0))
    # now move down the same number of lines as we have projects
    # plus one extra for the skipped line
    # this draws a line above the total
    translate(0, -myContentFontSize*myProjectLineHeight*(len(myProjects)+1) )
    line((0, 0), (contentWidth, 0))

# save a PDF with a fancy filename
# get rid of spaces in the customer name and then add invoice
outputFileName = customerData['Name'].replace(' ', '')+'_invoice.pdf'
saveImage(outputFileName)