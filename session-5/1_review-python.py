##############################
# python keywords: https://docs.python.org/3/reference/lexical_analysis.html#keywords
##############################
x = 'hello world'
##############################
# set variables
##############################
x = 10
y = 20
print('set variables', x, y)
print()

##############################
# augment variables
##############################
x += 20
y *= 20
print('augment variables', x, y)
print()

##############################
# execute functions
# python’s builtin functions: https://docs.python.org/3/library/functions.html
##############################
print('execute functions')
print('\t', 'print() is a function')
print('\t', 'len("abcd") =', len("abcd"))
print()

##############################
# define a function
# a great way to set aside a block of reusable code
# takes arguments, returns a thing if you want it to
##############################

print('define a function')
def myFunction(arg1, arg2='default'):
    #print(arg1, arg2)
    return arg1*2+arg2*2

myResults = myFunction('hi')
print('\t', myResults)
print('\t', myFunction(30, 3))
 
print()


##############################
# for loop
# for item in sequence:
##############################
print('loop through some numbers')
for myNumber in range(10):
    print('\t', myNumber)
print()

##############################
# conditional
##############################

print("Conditional statement")
randomNumber = randint(1, 6)
print('\t', 'The random number is', randomNumber)
if randomNumber > 3:
    print('\t', randomNumber, 'is greater than 3')
elif randomNumber == 1:
    print('\t', 'the number is one')
else:
    print('\t', randomNumber, 'is not 1, and is not greater than 3')

if randomNumber % 2 and randomNumber > 3:
    print('\t', randomNumber, 'is odd and greater than 3')
if randomNumber % 2 or randomNumber > 3:
    print('\t', randomNumber, 'is odd and/or it is greater than 3')


print()
# break a loop based on a conditional
print('Break a loop')   
for myNumber in range(100):
    print('\t', myNumber)
    if myNumber == 5:
        print('\t', 'ok let’s break the loop now')
        break
print()

# continue a loop based on a conditional    
print('Skip an item with continue')
for myNumber in range(10):
    if myNumber == 5:
        print('\t', 'skip it!')
        continue
    print('\t', myNumber)
        
print()

##############################
# while loop
# keep looping until a condition becomes false
# while condition:
##############################

print('let’s roll some dice until we roll a 6')
myNumber = None
myCount = 0
while myNumber != 6:
    myNumber = randint(1, 6)
    print('\t', myNumber)
    myCount += 1
tryWord = 'tries'
if myCount == 1:
    tryWord = 'try'
print('\t', 'we rolled a 6 so we can stop. It took', myCount, tryWord+'.')

    