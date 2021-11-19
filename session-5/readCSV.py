projectsPath = 'assets/projects.csv'
projectsPath = '/Users/david/Desktop/blah.txt'
customersPath = 'assets/customers.csv'

with open(projectsPath, 'w', encoding='utf-8') as projectsFile:
    projectsFile.write('hey i just overwrote this file')