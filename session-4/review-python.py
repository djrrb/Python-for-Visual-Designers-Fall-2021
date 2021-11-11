##############################
# set variables
##############################
x = 10
y = 20

##############################
# augment variables
##############################
x += 20
y *= 20

##############################
# execute functions
##############################
print('print() is a function')

##############################
# for loop
# for item in sequence:
##############################
print('loop through some numbers')
for myNumber in range(x):
    print('\t', myNumber)

##############################
# conditional
##############################

randomNumber = randint(1, 6)
if randomNumber > 3:
    print(randomNumber, 'is greater than 3')
elif randomNumber == 1:
    print('the number is one')
else:
    print(randomNumber, 'is not 1, and is not greater than 3')

# break a loop based on a conditional    
for myNumber in range(100):
    print('\t', myNumber)
    if myNumber > 10:
        print('\t', 'ok let’s break the loop now')
        break
    
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
print('we rolled a 6 so we stop. It look', myCount, 'tries')

##############################
# define a function
# a great way to set aside a block of reusable code
# takes arguments, returns a thing if you want it to
##############################

def myFunction(arg1, arg2='default'):
    return arg1*10+arg2*10
print(myFunction('hi'))
        
    
    