# draw every font that exists in a single folder
# use the OS module to read/write files and folders
import os

# define a path to look for
myPath = '../assets'

# list all the files in the folder
for myFileName in os.listdir(myPath):
    # if the filename is a TTF file
    if myFileName.endswith('.ttf'):
        # myFileName is just the filename
        # get the full path by joining the base path to the filename
        myFullPath = os.path.join(myPath, myFileName)
        print(myFileName)
        # make a document
        newPage()
        # set the font using the full path
        font(myFullPath, 100)
        # draw the text
        text(myFileName, (0, 0))
        
