flow = open("day17.txt", encoding="utf8").read().strip()
flowCounter = 0

grid = [['.']*7 for _ in range (3)]
grid.append(['-']*7)

rockCounter = -1
rockTypes = [
    [['.','.','@','@','@','@','.']],

    [['.','.','.','@','.','.','.'],
     ['.','.','@','@','@','.','.'],
     ['.','.','.','@','.','.','.']],

    [['.','.','.','.','@','.','.'],
     ['.','.','.','.','@','.','.'],
     ['.','.','@','@','@','.','.']],

    [['.','.','@','.','.','.','.'],
     ['.','.','@','.','.','.','.'],
     ['.','.','@','.','.','.','.'],
     ['.','.','@','.','.','.','.']],

    [['.','.','@','@','.','.','.'],
     ['.','.','@','@','.','.','.']]
]

def getIndexOfTopMostRock(grid):
    for i, e in enumerate(grid):
        if '#' in e or '-' in e:
            return i

def getIndexOfTopMostMovingRock(grid):
    for i, e in enumerate(grid):
        if '@' in e:
            return i

def drawRock(grid, rockCounter, rockTypes):
    index = getIndexOfTopMostRock(grid)

    if index < 8:
        for i in range(4):
            grid.insert(0,['.','.','.','.','.','.','.'])
        index = getIndexOfTopMostRock(grid)

    rockCounter += 1
    ri = rockCounter % len(rockTypes)
    rock = rockTypes[ri]
    if ri == 0:
        grid[index-4] = rock[0].copy()
    if ri == 1 or ri == 2:
        grid[index-6] = rock[0].copy()
        grid[index-5] = rock[1].copy()
        grid[index-4] = rock[2].copy()
    if ri== 3:
        grid[index - 7] = rock[0].copy()
        grid[index - 6] = rock[1].copy()
        grid[index - 5] = rock[2].copy()
        grid[index - 4] = rock[3].copy()
    if ri == 4:
        grid[index - 5] = rock[0].copy()
        grid[index - 4] = rock[1].copy()
    return rockCounter

def pushRock(grid, flowCounter, flow, rockCounter, rockTypes):
    f = flow[flowCounter % len(flow)]
    flowCounter += 1
    ri = rockCounter % len(rockTypes)
    index = getIndexOfTopMostMovingRock(grid)
    if f == '>':
        if ri == 0:
            rightIndex = len(grid[index])-grid[index][::-1].index('@')
            if rightIndex >= len(grid[index]):
                return flowCounter
            if grid[index][rightIndex] == '.':
                grid[index][rightIndex] = '@'
                grid[index][rightIndex-4] = '.'
        if ri == 1:
            rightIndex = len(grid[index])-grid[index][::-1].index('@')
            if rightIndex >= len(grid[index])-1:
                return flowCounter
            if grid[index][rightIndex] == '.' and grid[index+1][rightIndex+1] == '.' and grid[index+2][rightIndex] == '.':
                grid[index][rightIndex] = '@'
                grid[index + 1][rightIndex + 1] = '@'
                grid[index + 2][rightIndex] = '@'
                grid[index][rightIndex-1] = '.'
                grid[index + 1][rightIndex-2] = '.'
                grid[index + 2][rightIndex-1] = '.'
        if ri == 2:
            rightIndex = len(grid[index])-grid[index][::-1].index('@')
            if rightIndex >= len(grid[index]):
                return flowCounter
            if grid[index][rightIndex] == '.' and grid[index+1][rightIndex] == '.' and grid[index+2][rightIndex] == '.':
                grid[index][rightIndex] = '@'
                grid[index + 1][rightIndex] = '@'
                grid[index + 2][rightIndex] = '@'
                grid[index][rightIndex-1] = '.'
                grid[index + 1][rightIndex-1] = '.'
                grid[index + 2][rightIndex-3] = '.'
        if ri == 3:
            rightIndex = len(grid[index])-grid[index][::-1].index('@')
            if rightIndex >= len(grid[index]):
                return flowCounter
            if grid[index][rightIndex] == '.' and grid[index+1][rightIndex] == '.' and grid[index+2][rightIndex] == '.' and grid[index+3][rightIndex] == '.':
                grid[index][rightIndex] = '@'
                grid[index + 1][rightIndex] = '@'
                grid[index + 2][rightIndex] = '@'
                grid[index + 3][rightIndex] = '@'
                grid[index][rightIndex-1] = '.'
                grid[index + 1][rightIndex-1] = '.'
                grid[index + 2][rightIndex-1] = '.'
                grid[index + 3][rightIndex-1] = '.'
        if ri == 4:
            rightIndex = len(grid[index])-grid[index][::-1].index('@')
            if rightIndex >= len(grid[index]):
                return flowCounter
            if grid[index][rightIndex] == '.' and grid[index+1][rightIndex] == '.':
                grid[index][rightIndex] = '@'
                grid[index + 1][rightIndex] = '@'
                grid[index][rightIndex-2] = '.'
                grid[index + 1][rightIndex-2] = '.'
    elif f == '<':
        if ri == 0:
            leftIndex = grid[index].index('@')-1
            if leftIndex < 0:
                return flowCounter
            if grid[index][leftIndex] == '.':
                grid[index][leftIndex] = '@'
                grid[index][leftIndex+4] = '.'
        if ri == 1:
            leftIndex = grid[index].index('@')-1
            if leftIndex <= 0:
                return flowCounter
            if grid[index][leftIndex] == '.' and grid[index+1][leftIndex-1] == '.' and grid[index+2][leftIndex] == '.':
                grid[index][leftIndex] = '@'
                grid[index + 1][leftIndex - 1] = '@'
                grid[index + 2][leftIndex] = '@'
                grid[index][leftIndex+1] = '.'
                grid[index + 1][leftIndex+2] = '.'
                grid[index + 2][leftIndex+1] = '.'
        if ri == 2:
            leftIndex = grid[index].index('@')-1
            if leftIndex <= 1:
                return flowCounter
            if grid[index][leftIndex] == '.' and grid[index+1][leftIndex] == '.' and grid[index+2][leftIndex-2] == '.':
                grid[index][leftIndex] = '@'
                grid[index + 1][leftIndex] = '@'
                grid[index + 2][leftIndex-2] = '@'
                grid[index][leftIndex+1] = '.'
                grid[index + 1][leftIndex+1] = '.'
                grid[index + 2][leftIndex+1] = '.'
        if ri == 3:
            leftIndex = grid[index].index('@')-1
            if leftIndex < 0:
                return flowCounter
            if grid[index][leftIndex] == '.' and grid[index+1][leftIndex] == '.' and grid[index+2][leftIndex] == '.' and grid[index+3][leftIndex] == '.':
                grid[index][leftIndex] = '@'
                grid[index + 1][leftIndex] = '@'
                grid[index + 2][leftIndex] = '@'
                grid[index + 3][leftIndex] = '@'
                grid[index][leftIndex+1] = '.'
                grid[index + 1][leftIndex+1] = '.'
                grid[index + 2][leftIndex+1] = '.'
                grid[index + 3][leftIndex+1] = '.'
        if ri == 4:
            leftIndex = grid[index].index('@')-1
            if leftIndex < 0:
                return flowCounter
            if grid[index][leftIndex] == '.' and grid[index+1][leftIndex] == '.':
                grid[index][leftIndex] = '@'
                grid[index + 1][leftIndex] = '@'
                grid[index][leftIndex+2] = '.'
                grid[index + 1][leftIndex+2] = '.'
    return flowCounter

def dropRock(grid, rockCounter, rockTypes):
    ri = rockCounter % len(rockTypes)
    index = getIndexOfTopMostMovingRock(grid)
    if ri == 0:
        leftIndex = grid[index].index('@')
        if grid[index+1][leftIndex] == '.' and grid[index + 1][leftIndex+1] == '.' and grid[index + 1][leftIndex+2] == '.' and grid[index + 1][leftIndex+3] == '.':
            grid[index+1][leftIndex] = '@'
            grid[index + 1][leftIndex+1] = '@'
            grid[index + 1][leftIndex+2] = '@'
            grid[index + 1][leftIndex+3] = '@'
            grid[index][leftIndex] = '.'
            grid[index][leftIndex + 1] = '.'
            grid[index][leftIndex + 2] = '.'
            grid[index][leftIndex + 3] = '.'
        else:
            grid[index][leftIndex] = '#'
            grid[index][leftIndex + 1] = '#'
            grid[index][leftIndex + 2] = '#'
            grid[index][leftIndex + 3] = '#'
    if ri == 1:
        index += 2
        leftIndex = grid[index].index('@')
        if grid[index][leftIndex-1] == '.' and grid[index + 1][leftIndex] == '.' and grid[index][leftIndex+1] == '.':
            grid[index][leftIndex-1] = '@'
            grid[index + 1][leftIndex] = '@'
            grid[index][leftIndex+1] = '@'
            grid[index-1][leftIndex-1] = '.'
            grid[index-2][leftIndex] = '.'
            grid[index-1][leftIndex+1] = '.'
        else:
            grid[index-2][leftIndex] = '#'
            grid[index-1][leftIndex-1] = '#'
            grid[index - 1][leftIndex] = '#'
            grid[index - 1][leftIndex+1] = '#'
            grid[index][leftIndex] = '#'
    if ri == 2:
        index += 2
        leftIndex = grid[index].index('@')
        if grid[index+1][leftIndex] == '.' and grid[index + 1][leftIndex+1] == '.' and grid[index+1][leftIndex+2] == '.':
            grid[index+1][leftIndex] = '@'
            grid[index+1][leftIndex+1] = '@'
            grid[index+1][leftIndex+2] = '@'
            grid[index][leftIndex] = '.'
            grid[index][leftIndex+1] = '.'
            grid[index-2][leftIndex+2] = '.'
        else:
            grid[index][leftIndex] = '#'
            grid[index][leftIndex+1] = '#'
            grid[index][leftIndex+2] = '#'
            grid[index-1][leftIndex+2] = '#'
            grid[index-2][leftIndex+2] = '#'
    if ri == 3:
        index += 3
        leftIndex = grid[index].index('@')
        if grid[index+1][leftIndex] == '.':
            grid[index+1][leftIndex] = '@'
            grid[index-3][leftIndex] = '.'
        else:
            grid[index][leftIndex] = '#'
            grid[index-1][leftIndex] = '#'
            grid[index-2][leftIndex] = '#'
            grid[index-3][leftIndex] = '#'
    if ri == 4:
        index += 1
        leftIndex = grid[index].index('@')
        if grid[index+1][leftIndex] == '.' and grid[index+1][leftIndex+1] == '.':
            grid[index+1][leftIndex] = '@'
            grid[index+1][leftIndex+1] = '@'
            grid[index-1][leftIndex] = '.'
            grid[index-1][leftIndex+1] = '.'
        else:
            grid[index][leftIndex] = '#'
            grid[index][leftIndex+1] = '#'
            grid[index-1][leftIndex] = '#'
            grid[index-1][leftIndex+1] = '#'

def clearRows(grid, deletedRows):
    d = {}
    for i, l in enumerate(grid):
        for j, c in enumerate(l):
            if c == '#' and j not in d.keys():
                d[j] = i
    m = -1
    keys = d.keys()
    if 0 in keys and 1 in keys and 2 in keys and 3 in keys and 4 in keys and 5 in keys and 6 in keys:
        m = max(d[0],d[1],d[2],d[3],d[4],d[5],d[6])
    while m != -1 and grid[m+1] != ['-','-','-','-','-','-','-']:
        grid.pop(m+1)
        deletedRows += 1

    return grid, deletedRows



deletedRows = 0

for i in range(1000000):
    grid, deletedRows = clearRows(grid, deletedRows)
    rockCounter = drawRock(grid, rockCounter, rockTypes)
    while any('@' == value for row in grid for value in row):
        flowCounter = pushRock(grid, flowCounter, flow, rockCounter, rockTypes)
        dropRock(grid, rockCounter, rockTypes)


print(len(grid)-getIndexOfTopMostRock(grid)-1+deletedRows)