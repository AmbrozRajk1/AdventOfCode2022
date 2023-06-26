import sys

content = open("day7.txt", encoding="utf8").readlines()
dictionary = {}
spaceCounter = 0
space = '\t'
currentDirectory = []
uniqCounter = 1
totalSpace = 70000000
printQueueTotal = []

for line in content:
    line = line.replace('\n','')
    if line.startswith('$'): #command
        if line[2:].startswith('cd'): #change directory command
            nameOfDirectory = line[5:]
            if nameOfDirectory == '..':
                spaceCounter -= 1
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
print('Total disk space: {}'.format(totalSpace))
endDict = {}
needToDelete = 0
for elemToPrint in printQueueTotal:
    a,b = elemToPrint.replace("Total size of dir ","").replace(" is ","|").split('|')
    if (a == '/'):
        print('Used space of root dir {}: {}'.format(a, b))
        needToDelete = 30000000 - (totalSpace - int(b))
        print('Need to delete at least: {}'.format(needToDelete))
    endDict[a] = b

outDirName = ''
outDirSize = sys.maxsize
print('\nCandidates:')
for key in endDict.keys():
    if int(endDict[key]) > needToDelete:
        print('{}: {}'.format(key, endDict[key]))
        if int(endDict[key]) < outDirSize:
            outDirName = key
            outDirSize = int(endDict[key])

print("\nNeed to delete dir {} with size {}".format(outDirName, outDirSize))