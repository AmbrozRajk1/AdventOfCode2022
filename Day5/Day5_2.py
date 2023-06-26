f = open("day5.txt", encoding="utf8")
content = f.readlines()

stacks = [
    ['Z','T','F','R','W','J','G'],
    ['G','W','M'],
    ['J','N','H','G'],
    ['J','R','C','N','W'],
    ['W','F','S','B','G','Q','V','M'],
    ['S','R','T','D','V','W','C'],
    ['H','B','N','C','D','Z','G','V'],
    ['S','J','N','M','G','C'],
    ['G','P','N','W','C','J','D','L']
]

for line in content:
    numOfItems, fromStack, toStack = line.split('|')
    tempList = []
    for i in range(int(numOfItems)):
        tempList.append(stacks[int(fromStack)-1].pop())
    for item in reversed(tempList):
        stacks[int(toStack) - 1].append(item)

result = ''
for stack in stacks:
    result += stack[-1]

print(result)