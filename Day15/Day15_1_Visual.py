content = open("day15.txt", encoding="utf8").readlines()
B = []
S = []
grid = []
SToCheck = []
copiedToCheck = []

for i in range(55):
    list = []
    for j in range(71):
        list.append('.')
    grid.append(list)

for line in content:
    SX, SY, BX, BY = line.replace('Sensor at x=','').replace(', y=','|').replace(': closest beacon is at x=','|').replace(', y=1','|').replace('\n','').split('|')
    S.append((int(SX)+15,int(SY)+15))
    B.append((int(BX)+15,int(BY)+15))

    grid[int(SY)+15][int(SX)+15] = 'S'
    grid[int(BY)+15][int(BX)+15] = 'B'

tempS = []
bFound = False

#for t in S:
#r = [(23,22),(31,22)]
for z,t in S:
    tempS = [(z,t)]
    bFound = False
    while bFound == False:
        toCheck = tempS.copy()
        tempS.clear()
        for x,y in toCheck:
            if grid[y-1][x] in ('.', 'S', '#'):
                if grid[y-1][x] != 'S':
                    grid[y-1][x] = '#'
                if bFound == False:
                    tempS.append((x, y-1))
            elif grid[y-1][x] == 'B':
                bFound = True

            if grid[y+1][x] in ('.', 'S', '#'):
                if grid[y+1][x] != 'S':
                    grid[y+1][x] = '#'
                if bFound == False:
                    tempS.append((x, y+1))
            elif grid[y+1][x] == 'B':
                bFound = True

            if grid[y][x-1] in ('.', 'S', '#'):
                if grid[y][x-1] != 'S':
                    grid[y][x-1] = '#'
                if bFound == False:
                    tempS.append((x-1, y))
            elif grid[y][x-1] == 'B':
                bFound = True

            if grid[y][x+1] in ('.', 'S', '#'):
                if grid[y][x+1] != 'S':
                    grid[y][x+1] = '#'
                if bFound == False:
                    tempS.append((x+1, y))
            elif grid[y][x-1] == 'B':
                bFound = True

for e in grid:
    print(''.join(e))

