redColor = .5, 0, 0
grayColor = .4, .4, .4
greenColor = 0, .1, 0

blendMode('overlay')

t = 15
ph = 200
pw = 200

for x in range(0, width(), pw):
    with savedState():
        for y in range(0, height(), ph):

            # vertical bars
            fill(*grayColor)
            rect(0, 0, t, ph)
            fill(*greenColor)
            rect(2*t, 0, t*2, ph)
            fill(*redColor)
            rect(6*t, 0, t, ph)
            fill(*grayColor)
            rect(8*t, 0, t*2, ph)

            # horizontal bars
            fill(*grayColor)
            rect(0, 0, pw, t)
            fill(*greenColor)
            rect(0, 2*t, pw, t*2)
            fill(*redColor)
            rect(0, 6*t, pw, t)
            fill(*grayColor)
            rect(0, 8*t, pw, t*2)
    
            translate(0, ph)
    translate(pw, 0)
