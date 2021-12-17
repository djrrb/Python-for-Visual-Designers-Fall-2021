myPals = {
    'darkmode':
        {
            'foreground': (1, 0, 0),
            'background': (0, 1, 0),
        },
        
    'lightmode': 
        {
            'foreground': (1, 1, 1),
            'background': (0, 0, 0),
            },
            
    'locontrastmode': 
        {
            'foreground': (1, 1, 1),
            'background': (.8, .8, .8),
            }
            
            
            
    }
    
palName = 'locontrastmode'

fill(*myPals[palName]['background'])
rect(0, 0, width(), height())

fill(*myPals[palName]['foreground'])
oval(200, 200, 400, 400)