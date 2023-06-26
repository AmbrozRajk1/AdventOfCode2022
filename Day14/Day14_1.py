content = open("day14.txt", encoding="utf8").readlines()
grid = []
sandInputOffset = -400
gridWidth = 200
gridHeight = 200
for i in range(gridHeight+1):
    list = []
    for j in range(gridWidth+1):
        list.append('.')
    grid.append(list)

def getSandLandingCoordinates(tuple):
    x, y = tuple
    if grid[y+1][x] == '.':
        return getSandLandingCoordinates((x,y+1))
    if grid[y+1][x] in ('#','o') and grid[y+1][x-1] == '.':
        return getSandLandingCoordinates((x-1,y+1))
    if grid[y+1][x] in ('#','o') and grid[y+1][x-1] in ('#','o') and grid[y+1][x+1] == '.':
        return getSandLandingCoordinates((x+1,y+1))
    if grid[y+1][x] in ('#','o') and grid[y+1][x-1] in ('#','o') and grid[y+1][x+1] in ('#','o'):
        return (x,y)

grid[0][500+sandInputOffset] = '+'

for line in content:
    listOfCoordinates = line.replace('\n','').split(' -> ')
    for i in range(len(listOfCoordinates)-1):
        startX, startY = listOfCoordinates[i].split(',')
        startX = int(startX)+sandInputOffset
        startY = int(startY)
        endX, endY = listOfCoordinates[i+1].split(',')
        endX = int(endX)+sandInputOffset
        endY = int(endY)

        if startX == endX:
            if startY < endY:
                for k in range(startY,endY+1):
                    grid[k][startX] = '#'
            else:
                for k in range(endY,startY+1):
                    grid[k][startX] = '#'
        elif startY == endY:
            if startX < endX:
                for k in range(startX,endX+1):
                    grid[startY][k] = '#'
            else:
                for k in range(endX,startX+1):
                    grid[startY][k] = '#'

result = 0

for l in range((gridWidth*gridHeight)//2):
    try:
        nextX, nextY = getSandLandingCoordinates((500+sandInputOffset,0))
        grid[nextY][nextX] = 'o'
    except:
        result = l
        break
for e in grid:
    print(''.join(e))

print('\nCount of sand grains: {}'.format(result))