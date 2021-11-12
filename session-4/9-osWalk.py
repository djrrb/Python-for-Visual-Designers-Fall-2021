import os

# get a path
# this can be absolute or relative
# two dots will go up one folder to the main directory
myPath = '..'

# walk through the folders and files
# this is different than listdir() because it will also go into subdirectories
for root, dirs, files in os.walk(myPath):
    # loop through all the files
    for file in files:
        # if the file is a PNG
        if file.endswith('.png'):
            # print the filename
            print(file)
            # get the full path by joining the root to the filename
            myImagePath = os.path.join(root, file)
            # draw the image to a new page
            newPage()
            image(myImagePath, (0, 0))