ourNames = """Mei
Ladan
Ashley
Noelle
Gerben
charity
Courtney
Andrea
Andrew
Anna 
Chag Chag
Marget
Lauren
Masahiro
Morgan
Vikki
Kevin"""

nameList = ourNames.split('\n')
import random
random.shuffle(nameList)
for name in nameList:
    print(name)
