
newPage(1000, 1000)
x = 0
y = 0

for anotherLetter in 'helloworld':
    for letter in 'helloworld':
        print(letter)
        fill(random(), random(), random())
        oval(x, y, 100, 100)
        x = x + 100
    y = y + 100
    x = 0

print('done')

#saveImage('~/desktop/myFileName.png')
