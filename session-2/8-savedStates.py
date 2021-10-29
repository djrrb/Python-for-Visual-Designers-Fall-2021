# set up my base styles
# green
fill(0, 1, 0)
font('Georgia', 100)
text('hello world', (0, 0))

# make a saved state
# this will save my formatting as i have it
# and allow me to return to it
with savedState():
    # now do a bunch of additional stuff
    # move to the center
    translate(width()/2, height()/2)
    # make some other transformations
    fill(1, 0, 0) # red fill
    stroke(0) # black stroke
    rotate(30) # 30 degree rotation
    # now draw a box and some white text
    rect(-250, -250, 500, 500)
    fill(1)
    text('more text!', (0, 0), align="center")

# thse second I dedent, I go back to my original formatting
# drawing from the bottom left in green
# this means I don’t have to manually undo any of the transformations done above, I just go back
oval(0, 0, 100, 100)