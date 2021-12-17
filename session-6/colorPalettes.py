# color palette example
# a dictionary of dictionaries

myPals = {
    'darkmode': # palette name
        {
            'foreground': (1, 0, 0), # color name: color value
            'background': (0, 1, 0), # color name: color value
        },
        
    'lightmode': # palette name
        {
            'foreground': (1, 1, 1), # color name: color value
            'background': (0, 0, 0), # color name: color value
            },
            
    'locontrastmode': # palette name
        {
            'foreground': (1, 1, 1), # color name: color value
            'background': (.8, .8, .8), # color name: color value
            }
            
            
            
    }

# what palette should we use
palName = 'locontrastmode'

# draw a background shape using my palette
fill(*myPals[palName]['background'])
rect(0, 0, width(), height())

# draw a foreground shape using my palette
fill(*myPals[palName]['foreground'])
oval(200, 200, 400, 400)