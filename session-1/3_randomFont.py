import random

inch = 72
newPage(8.5*inch, 11*inch)

# how many fonts do i have?

installedFonts()
print(len(installedFonts()))

# choose one installed font and print it
#print(random.choice(installedFonts()))

myInstalledFonts = installedFonts()
randomFont = random.choice(myInstalledFonts)

font(randomFont)
fontSize(100)
text('hello', (0, 130))


randomFont = random.choice(myInstalledFonts)

font(randomFont)
fontSize(100)
text('world', (0, 0))
