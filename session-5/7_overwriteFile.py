filePath = 'blah.txt'
with open(filePath, 'w', encoding='utf-8') as myFile:
    myFile.write('hey i just overwrote this file')