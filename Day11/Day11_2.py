import math

content = open("day11.txt", encoding="utf8").readlines()
listOfMonkeys = []
round = 0
listOfTestNumber = []

class Monkey:
    id = -1
    items = []
    operationType = ''
    operationNumber = -1
    test = -1
    ifTestTrue = -1
    ifTestFalse = -1
    inspectedItems = 0

for i in range(0,len(content),7):
    m = Monkey()
    splittedLine = content[i].replace('\n','').split(' ')
    m.id = splittedLine[1].replace(':','')
    listOfStaringItems = content[i+1].replace('\n','').split(' ')
    listOfItems = []
    for i1,e in enumerate(listOfStaringItems):
        if i1 != 0 and i1 != 1 and i1 != 2 and i1 != 3:
            listOfItems.append(e.replace(',',''))
    m.items = listOfItems.copy()
    splittedLine = content[i+2].replace('\n','').split(' ')
    m.operationType = splittedLine[6]
    m.operationNumber = splittedLine[7]
    splittedLine = content[i+3].replace('\n','').split(' ')
    m.test = splittedLine[5]
    listOfTestNumber.append(int(m.test))
    splittedLine = content[i+4].replace('\n','').split(' ')
    m.ifTestTrue = splittedLine[9]
    splittedLine = content[i+5].replace('\n','').split(' ')
    m.ifTestFalse = splittedLine[9]

    listOfMonkeys.append(m)

devidor = math.prod(listOfTestNumber)

for i in range(10000):
    for monkey in listOfMonkeys:
        for item in monkey.items:
            worry = int(item)
            if monkey.operationType == '*':
                if monkey.operationNumber == 'old':
                    worry = worry * worry
                else:
                    worry = worry * int(monkey.operationNumber)
                worry = worry % devidor
                if worry % int(monkey.test) == 0:
                    for m in listOfMonkeys:
                        if m.id == monkey.ifTestTrue:
                            m.items.append(worry)
                            break
                else:
                    for m in listOfMonkeys:
                        if m.id == monkey.ifTestFalse:
                            m.items.append(worry)
                            break
            elif monkey.operationType == '+':
                if monkey.operationNumber == 'old':
                    worry = worry * tempWorry
                else:
                    worry = worry + int(monkey.operationNumber)
                worry = worry % devidor
                if worry % int(monkey.test) == 0:
                    for m in listOfMonkeys:
                        if m.id == monkey.ifTestTrue:
                            m.items.append(worry)
                            break
                else:
                    for m in listOfMonkeys:
                        if m.id == monkey.ifTestFalse:
                            m.items.append(worry)
                            break
            monkey.inspectedItems += 1
        monkey.items = []

listOfInspectedItems = []
for m in listOfMonkeys:
    print(m.id, m.inspectedItems)
    listOfInspectedItems.append(m.inspectedItems)

listOfInspectedItems.sort()
print('Monkey business is: {}'.format(listOfInspectedItems[-1]*listOfInspectedItems[-2]))


