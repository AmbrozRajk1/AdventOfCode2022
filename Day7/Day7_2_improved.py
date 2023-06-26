content = open("day7.txt", encoding="utf8").readlines()
folderDict, currentDirectory, dirSizes, uniqCounter = {}, [], [], 1

for line in content:
    if line.replace('\n','').startswith('$ cd'): #command
        nameOfDirectory = line.replace('\n','')[5:]
        if nameOfDirectory == '..':
            dirSizes.append(int(folderDict[currentDirectory[-1]]))
            del folderDict[currentDirectory[-1]]
            currentDirectory.pop()
        else:
            if nameOfDirectory in folderDict.keys():
                currentDirectory.append("{}_{}".format(nameOfDirectory,uniqCounter))
                folderDict["{}_{}".format(nameOfDirectory, uniqCounter)] = 0
                uniqCounter+=1
            else:
                currentDirectory.append(nameOfDirectory)
                folderDict[nameOfDirectory] = 0
    elif line[0].isdigit(): #file
        fileSize, fileName = line.replace('\n','').split(' ')
        for key in folderDict:
            folderDict[key] += int(fileSize)

dirSizes.sort()
print(next("Need to delete dir with size {}".format(size) for size in dirSizes if size > 30000000 - (70000000 - max(dirSizes))))