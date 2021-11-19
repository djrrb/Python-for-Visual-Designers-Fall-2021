myDict = {
    'oranges': 2,
    'bananas': 8,
    'apples': 3,
    }
    
print(myDict['oranges'])
myDict['kiwi'] = 10

for key, value in myDict.items():
    print(key, value)
    
for key in myDict:
    value = myDict[key]
    print(key, value)