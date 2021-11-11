####################################
# integers and floating point number
# unmutable
####################################
print('='*10, 'INTEGERS', '='*10)
myInt = 5.5
print('x+2 =', myInt+2)
print('x-2 =', myInt-2)
print('x*2 =', myInt*2)
print('x/2 =', myInt/2, 'this will always be a float')
print('x//2 =', myInt//2, '(how many times does x go in to y?)')
print('x%2 =', myInt%2, '(what is the remainder?)')

print()
##################################
# a string is a sequence of characters
# unmutable
####################################
print('='*10, 'STRINGS', '='*10)

myString = 'Hello World'
print('first character of string:', myString[0])
print('last character of string:', myString[-1])
print('last five character of string:', myString[-5:])
print('reversed string:', myString[::-1])
print('capitalized string:', myString.upper())
print('lowercase string:', myString.lower())
print('is \'e\' in string?', 'e' in myString)
print('loop through string:')
for myCharacter in myString:
    print('\t', myCharacter)
print('convert string to list', list(myString))
    
print()
#######################################
# a list is a sequence of other objects
# mutable
#######################################
print('='*10, 'LISTS', '='*10)
myList = [
    'oranges',
    'apples',
    'bananas',
    ]
myOriginalList = myList[:] # make a copy of list
# append item to list
myList.append('nectarine')
print('length of list:', myList[0])
print('first item in list:', myList[0])
print('last character of list:', myList[-1])
print('first two items in string:', myList[:2])
print('did pears make the list?', 'pears' in myList)
myList.sort()
print('sort list:', myList)
myList.reverse()
print('reverse list:', myList)
print('original list from copy:', myOriginalList)

print()
#######################################
# a dictionary maps keys to values
# mutable
#######################################
print('='*10, 'DICTIONARIES', '='*10)
myDict = {
    'apples': 3,
    'oranges': 2,
    'bananas': 8,
    }
print(myDict)
myOriginalDict = myDict.copy() # make a copy of ict
print('length of dictionary:', len(myDict))
print('does key exist in dict:', 'blackberries' in myDict)
print('query dictionary by key:', myDict['bananas'])
# add to/edit dictionary
myDict['papayas'] = 2
# remove from dictionary
del myDict['oranges']
print('get a list of keys', myDict.keys())
print('get a list of key, value tuples', myDict.items())
print('original dict:', myOriginalDict)

print()
#######################################
# a tuple groups objects unmutably
# like a list, but unmutable
#######################################
print('='*10, 'TUPLES', '='*10)
myTuple = (1, 0, .5)
print(myTuple)
print('length of tuple:', len(myTuple))
print('first item in tuple:', myTuple[0])
print('last item in tuple:', myTuple[-1])
print('unpack tuple:', *myTuple)
r, g, b = myTuple
print('unpack tuple into mupltiple variables', r,g,b)
print('loop through items in tuple:')
for myItem in myTuple:
    print('\t', myItem)

print()
####################################
# True, False (booleans), None
# unmutable
####################################
print('='*10, 'TRUE, FALSE, NONE', '='*10)
print('Test conditions, such as 5>2:', 5>2)
print('Test equivalence, such as "a"=="b":', "peanut butter"=="jelly")
print('Test truthiness:')
myValues = [None, 0, 1, 2, 3, True, False]
for myValue in myValues:
    if myValue:
        print('\t', myValue, 'is truthy.')
    else:
        print('\t', myValue, 'is falsy.')
    