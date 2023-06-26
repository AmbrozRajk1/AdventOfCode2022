import numpy as np

def getSteps(p):
    s = ""
    for i, t in enumerate(p):
        if t.isdigit():
            s += t
        else:
            return (p[i+1:],int(s),t)

def move(grid,steps,turn,x,y,direction):
    if x == 200 and y<50: x=0; y=y+100; direction='DOWN'
    if y == 150 and x<50: x=149-x; y=99; direction='LEFT'
    if x == -1 and y>=50 and y<100: x=y+100; y=0; direction='RIGHT'
    if x == -1 and y>=100 and y<150: x=149; y=y-100; direction='UP'
    if y == -1 and x>=100 and x<150: x=149-x; y=50; direction='RIGHT'
    if y == -1 and x>=150 and x<200: x=0; y=y-100; direction='DOWN'

    #DODELAJ
    if direction == 'RIGHT':
        grid[x,y] = '>'
        for i in range(steps):
            if y+1 == rowLength:
                y = -1
            if grid[x,y+1] == '#':
                continue
            elif grid[x,y+1] == ' ':
                y_tmp = np.where((grid[x,:] == '.') | (grid[x,:] == '>') | (grid[x,:] == '<') | (grid[x,:] == 'v') | (grid[x,:] == '^') | (grid[x,:] == '#'))[0][0]
                if grid[x,y_tmp] == '#':
                    continue
                else:
                    grid[x,y_tmp] = '>'
                    y = y_tmp
            elif grid[x,y+1] in ['.','>','<','v','^']:
                grid[x,y+1] = '>'
                y = y+1
        if turn == 'R':
            direction = 'DOWN'
        elif turn == 'L':
            direction = 'UP'
    elif direction == 'LEFT':
        grid[x,y] = '<'
        for i in range(steps):
            if y-1 == -1:
                y = rowLength
            if grid[x,y-1] == '#':
                continue
            elif grid[x,y-1] == ' ':
                y_tmp = np.where((grid[x,:] == '.') | (grid[x,:] == '>') | (grid[x,:] == '<') | (grid[x,:] == 'v') | (grid[x,:] == '^') | (grid[x,:] == '#'))[0][-1]
                if grid[x,y_tmp] == '#':
                    continue
                else:
                    grid[x,y_tmp] = '<'
                    y = y_tmp
            elif grid[x,y-1] in ['.','>','<','v','^']:
                grid[x,y-1] = '<'
                y = y-1
        if turn == 'R':
            direction = 'UP'
        elif turn == 'L':
            direction = 'DOWN'
    elif direction == 'DOWN':
        grid[x,y] = 'v'
        for i in range(steps):
            if x+1 == nrows:
                x = -1
            if grid[x+1,y] == '#':
                continue
            elif grid[x+1,y] == ' ':
                x_tmp = np.where((grid[:,y] == '.') | (grid[:,y] == '>') | (grid[:,y] == '<') | (grid[:,y] == 'v') | (grid[:,y] == '^') | (grid[:,y] == '#'))[0][0]
                if grid[x_tmp,y] == '#':
                    continue
                else:
                    grid[x_tmp,y] = 'v'
                    x = x_tmp
            elif grid[x+1,y] in ['.','>','<','v','^']:
                grid[x+1,y] = 'v'
                x = x+1
        if turn == 'R':
            direction = 'LEFT'
        elif turn == 'L':
            direction = 'RIGHT'
    elif direction == 'UP':
        grid[x,y] = '^'
        for i in range(steps):
            if x-1 == -1:
                x = nrows
            if grid[x-1,y] == '#':
                continue
            elif grid[x-1,y] == ' ':
                x_tmp = np.where((grid[:,y] == '.') | (grid[:,y] == '>') | (grid[:,y] == '<') | (grid[:,y] == 'v') | (grid[:,y] == '^') | (grid[:,y] == '#'))[0][-1]
                if grid[x_tmp,y] == '#':
                    continue
                else:
                    grid[x_tmp,y] = 'v'
                    x = x_tmp
            elif grid[x-1,y] in ['.','>','<','v','^']:
                grid[x-1,y] = 'v'
                x = x-1
        if turn == 'R':
            direction = 'RIGHT'
        elif turn == 'L':
            direction = 'LEFT'


content = [line.replace("\n","") for line in open("day22.txt", encoding="utf8").readlines()]
nrows = len(content)-2
rowLength = max(len(line) for line in content[:-2])

path = content[-1] + 'F'
grid = np.full((nrows, rowLength), ' ', dtype=str)

#populate grid
for i, line in enumerate(content[:-2]):
    for j, char in enumerate(line):
        grid[i, j] = char

#find coordinates of first dot
x_start = -1
y_start = -1
for i, line in enumerate(grid):
    if '.' in line:
        x_start = i
        y_start = np.where(line == '.')[0][0]
        break


#get steps and direction
x = x_start
y = y_start
direction = 'RIGHT'

while len(path) > 0:
    path, steps, turn = getSteps(path)
    while movesLeft > 0:
        movesLeft = move(grid,steps,turn,x,y,direction)


total = ((x+1)*1000) + ((y+1)*4)
if direction == 'RIGHT': total += 0
if direction == 'DOWN': total += 1
if direction == 'LEFT': total += 2
if direction == 'UP': total += 3
print(total)

