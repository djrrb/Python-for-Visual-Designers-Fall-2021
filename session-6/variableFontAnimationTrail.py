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

# set the text string we will draw
myString = 'R'

# set relative font path
myFontPath = '../assets/CondorVariable-VF.ttf'

# loop through frames
for myFrame in range(myFrames):
    # make a new page and a background
    newPage()
    fill(.2)
    rect(0, 0, width(), height())

    # set the font and make it big
    font(myFontPath, 800)
    # in a saved state
    with savedState():
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
            # also set the weight and italic value of the letter
            # that we will draw
            # remap(value, start1, stop1, start2, stop2)
            wghtValue = remap(yMultiplier, -1, 1, 200, 900)
            wdthValue = remap(yMultiplier, -1, 1, 50, 150)
            italValue = remap(yMultiplier, -1, 1, 0, 1)
            fontVariations(wght=wghtValue, wdth=wdthValue, ital=italValue)
            stroke(.8, 1, 1)
            strokeWidth(1)
            fill(None)
            text(myString, (width()/2, 200), align="center")
            if myPhase == myFrame:
                # store the values for the emphasis frame
                theFrameWghtValue = wghtValue
                theFrameWdthValue = wdthValue
                theFrameItalValue = italValue
        # draw the text at the end so it's on top
        fill(1)
        stroke(None)
        # use the values we stored earlier
        fontVariations(wght=theFrameWghtValue, wdth=theFrameWdthValue, ital=theFrameItalValue)
        text(myString, (width()/2, 200), align="center")
        
 

# save gif
saveImage('variableFontAnimationTrail.gif')