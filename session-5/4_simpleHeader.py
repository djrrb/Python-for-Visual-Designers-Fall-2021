def drawHeader(chapterTitle=''):
    # draw header is a function with one optional argument.
    # if that argument is not provided, it will default to an empty string
    font('Times New Roman', 20)
    headerToPrint = 'This is a header'
    # if we are given a chapter title, add it to the string we will print
    if chapterTitle:
        headerToPrint += ' | ' + chapterTitle
    # draw the text
    text(headerToPrint, (20, height()-40))

# make some pages
newPage()
drawHeader()

# cool to reuse the code each time
newPage()
drawHeader()

# this time, add an optional argument to the header
newPage()
drawHeader('Optional Chapter Title!')

# drawHeader() returns nothing
print(drawHeader())