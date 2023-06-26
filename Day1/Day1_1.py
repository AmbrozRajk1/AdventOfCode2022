f = open("day1.txt", encoding="utf8")
content = f.read().split('\n\n')
listOfSums =  []

for elf in content:
    totalSum = 0
    for num in elf.split('\n'):
        totalSum = totalSum + int(num)
    listOfSums.append(totalSum)

listOfSums.sort()
print(listOfSums[-1])