# set a single RGB variable as a tuple
myRgb = (1, 0, 0)
# manually unpack it
myR, myG, myB = myRgb
fill(myR, myG, myB)
# manually unpack a different way
myR = myRgb[0]
myG = myRgb[1]
myB = myRgb[2]
fill(myR, myG, myB)
# or auto-unpack it
fill(*myRgb)

rect(0, 0, 50, 50)

# set two variables at once
x = y = 500
# x = 500
# y = 500
print(x, y)

# or unpack a tuple as you make it
x, y = 500, 500
print(x, y)