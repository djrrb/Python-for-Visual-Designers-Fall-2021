import random

# how many fonts do i have?

installedFonts()
print(len(installedFonts()))

# choose one installed font and print it
#print(random.choice(installedFonts()))

myInstalledFonts = installedFonts()
randomFont = random.choice(myInstalledFonts)

print(randomFont)
font(randomFont)
fontSize(100)
text('hello world', (0, 0))
