# Released by DJR under the BSD license 
def lerp(start, stop, amt):
	"""
	Return the interpolation factor (between 0 and 1) of a VALUE between START and STOP.
	https://processing.org/reference/lerp_.html
	"""
	return float(amt-start) / float(stop-start)
	
def norm(value, start, stop):
	"""
	Interpolate using a value between 0 and 1
	See also: https://processing.org/reference/norm_.html
	"""
	return start + (stop-start) * value

def remap(value, start1, stop1, start2, stop2, withinBounds=False):
    """
    Re-maps a number from one range to another.
    """
    factor = lerp(start1, stop1, value)
    if withinBounds:
        if factor < 0: factor = 0
        if factor > 1: factor = 1
    return norm(factor, start2, stop2)


# set number of frames
myFrames = 30

# set relative font path
myFontPath = '../assets/CondorVariable-VF.ttf'

# loop through frames
for myFrame in range(myFrames):
    # make a new page and a background
    newPage()
    fill(1)
    rect(0, 0, width(), height())

    # set the font and make it big
    font(myFontPath, 800)
    # in a saved state, move to the vertical center of the canvas
    with savedState():
        translate(0, height()/2)
        # set a starting point for x, we will make it bigger
        x = 0
        # now draw each position in the wave
        for myPhase in range(myFrames):
            # get a multiplier using the sin() function
            # 2*pi = full circle
            # myPhase/myFrames = where I am at in the cycle
            yMultiplier = sin(2*pi*myPhase/myFrames)
            # mutiply this by half the height so the wave can go up and down to fill the canvas
            y = yMultiplier*height()/2
            # if we are on the “key” frame where the page we are drawing matches the dot
            if myPhase == myFrame:
                # make it big and red
                fill(1, 0, 0)
                stroke(None)
                oval(x-40, y-40, 80, 80)
                # also set the weight and italic value of the letter
                # that we will draw
                # use the remap function to take the (-1, 1) range and map it to the range of the axis
                wghtValue = remap(yMultiplier, -1, 1, 200, 900)
                italValue = remap(yMultiplier, -1, 1, 0, 1)
            else:
                # draw all other frames as small light gray circles
                stroke(.8)
                strokeWidth(2)
                fill(None)
                oval(x-20, y-20, 40, 40)
            # change the x value 
            x += width()/myFrames
        
    # only once per frame, set the font
    fontVariations(wght=wghtValue, ital=italValue)
    # make it blue
    fill(0, 0, 1)
    # draw the text
    text('a', (width()/2, 300), align="center")

# save gif
saveImage('variableFontAnimation.gif')