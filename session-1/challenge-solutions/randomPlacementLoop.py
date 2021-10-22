fontSize(100)
font('MinionPro-Regular')
for letter in 'hello world'*10:
    x = random()*width()
    y = random()*height()
    print(letter, x, y)
    fill(random(), random(), random())
    text(letter, (x, y))