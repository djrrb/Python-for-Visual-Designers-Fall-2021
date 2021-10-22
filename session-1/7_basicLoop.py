# make a new page
newPage(1000, 1000)

# set our x and y to 0
# we will redefine these variables
# to draw our shapes at different positions
x = 0
y = 0

# we are gonna loop through a string

# Python: for letter in 'hello world':
# English: "for each letter in the string "helloworld", do the following:

# for = the python keyword to begin a for loop

# letter = a variable name (can be anything) that will change during each iteration of our loop

# in = a python keyword to denote that something is part of or included in another thing

# 'hello world' = just a string, but it can be any sequence.

# : = this line ends in a colon, denoting that the indented lines that follow will be part of the loop

for letter in 'helloworld':
    # this code will be run for each letter
    # print the letters one at a time
    print(letter, x)
    # make it a random color
    # we call random() 3 times, for red, green, and blue
    fill(random(), random(), random())
    # draw an oval
    oval(x, y, 100, 100)
    # move x over each time so that they don’t draw on top of each other
    x = x + 100

# at the very end, we can dedent
# this exits the loop, and now the code that follows
# will only be run once
print('done')
