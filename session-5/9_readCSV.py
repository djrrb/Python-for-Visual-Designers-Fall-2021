import csv

customerToDisplay = 2

projectsPath = 'assets/projects.csv'
customersPath = 'assets/customers.csv'

print("INVOICE")
print("="*20)

with open(projectsPath, 'r', encoding='utf-8') as projectsFile:
    projectsReader = csv.reader(projectsFile)
    
    with open(customersPath, 'r', encoding='utf-8') as customersFile:
        customersReader = csv.reader(customersFile)
    
        for customerIndex, customerRow in enumerate(customersReader):
            if customerIndex == 0:
                continue
            if int(customerRow[0]) == customerToDisplay:
                print('To:', customerRow[1])
                print(customerRow[2])
                print(customerRow[3])
    print('='*20)
    
    totalCost = 0
    for projectIndex, projectRow in enumerate(projectsReader):
        #print(projectIndex, projectRow)
        idNumber, name, customer, date, cost, paid, notes = projectRow
        
        if projectIndex == 0:
            continue
        if int(customer) == customerToDisplay:
            print(name, cost)
            