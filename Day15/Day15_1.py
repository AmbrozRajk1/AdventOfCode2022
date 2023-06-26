content = open("day15.txt", encoding="utf8").readlines()
B = []
S = []
grid = []
SToCheck = []
copiedToCheck = []


for line in content:
    SX, SY, BX, BY = line.replace('Sensor at x=','').replace(', y=','|').replace(': closest beacon is at x=','|').replace(', y=1','|').replace('\n','').split('|')
    S.append((int(SX),int(SY)))
    B.append((int(BX),int(BY)))

tempS = []
bFound = False
allChecked = set()
#for t in S:
#r = [(23,22),(31,22)]
sCount = 0
for z,t in S:
    sCount += 1
    tempS = [(z,t)]
    alreadyChecked = [(z,t)]
    print('Checking sensor {}/{}.'.format(sCount,len(S)))
    bFound = False
    while bFound == False:
        toCheck = tempS.copy()
        tempS.clear()
        for x,y in toCheck:
            if (x,y-1) not in B:
                if bFound == False:
                    if (x,y-1) not in alreadyChecked: tempS.append((x,y-1)); alreadyChecked.append((x,y-1))
                    allChecked.add((x,y-1))
            elif (x,y-1) in B:
                bFound = True
                allChecked.add((x,y-1))

            if (x,y+1) not in B:
                if bFound == False:
                    if (x,y+1) not in alreadyChecked: tempS.append((x,y+1)); alreadyChecked.append((x,y+1))
                    allChecked.add((x,y+1))
            elif (x,y+1) in B:
                bFound = True
                allChecked.add((x,y+1))

            if (x-1,y) not in B:
                if bFound == False:
                    if (x-1,y) not in alreadyChecked: tempS.append((x-1,y)); alreadyChecked.append((x-1,y))
                    allChecked.add((x-1,y))
            elif (x-1,y) in B:
                bFound = True
                allChecked.add((x-1,y))

            if (x+1,y) not in B:
                if bFound == False:
                    if (x+1,y) not in alreadyChecked: tempS.append((x+1,y)); alreadyChecked.append((x+1,y))
                    allChecked.add((x+1,y))
            elif (x+1,y) in B:
                bFound = True
                allChecked.add((x+1,y))

count = 0
for x,y in allChecked:
    if y == 2000000:
        count+=1

print("\n{}".format(count))
#for e in grid:
#    print(''.join(e))

