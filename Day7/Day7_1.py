content = open("day7.txt", encoding="utf8").readlines()
dictionary = {}
spaceCounter = 0
space = '\t'
currentDirectory = []
uniqCounter = 1
totalCountOutput = 0
printQueueTotal = []

for line in content:
    line = line.replace('\n','')
    if line.startswith('$'): #command
        if line[2:].startswith('cd'): #change directory command
            nameOfDirectory = line[5:]
            if nameOfDirectory == '..':
                spaceCounter -= 1
                if dictionary[currentDirectory[-1]] <= 100000:
                    totalCountOutput += dictionary[currentDirectory[-1]]
                printQueueTotal.append("Total size of dir {} is {}".format(currentDirectory[-1],dictionary[currentDirectory[-1]]))
                del dictionary[currentDirectory[-1]]
                currentDirectory.pop()
            else:
                if nameOfDirectory in dictionary.keys():
                    currentDirectory.append("{}_{}".format(nameOfDirectory,uniqCounter))
                    print("{}- {} (dir)".format(space * spaceCounter, "{}_{}".format(nameOfDirectory,uniqCounter)))
                    dictionary["{}_{}".format(nameOfDirectory,uniqCounter)] = 0
                    spaceCounter += 1
                    uniqCounter+=1
                else:
                    currentDirectory.append(nameOfDirectory)
                    print("{}- {} (dir)".format(space * spaceCounter, nameOfDirectory))
                    dictionary[nameOfDirectory] = 0
                    spaceCounter += 1
    elif line[0].isdigit(): #file
        fileSize, fileName = line.split(' ')
        print("{}- {} (file, size={})".format(space * spaceCounter, fileName, fileSize))
        for key in dictionary:
            dictionary[key] += int(fileSize)
print('\n')
for elemToPrint in printQueueTotal:
    print(elemToPrint)
print('\nSum of total sizes of dirs with a total size of at most 100000 is: {}'.format(totalCountOutput))