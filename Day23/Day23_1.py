import numpy as np
from collections import defaultdict

def allNeighboursEmpty(g,x,y):
    if grid[x+1, y-1] == '#': return False
    if grid[x+1,y] == '#': return False
    if grid[x+1, y+1] == '#': return False
    if grid[x,y+1] == '#': return False
    if grid[x-1,y+1] == '#': return False
    if grid[x-1,y] == '#': return False
    if grid[x-1,y-1] == '#': return False
    if grid[x,y-1] == '#': return False
    return True

def canMove(g,x,y,d):
    if d == 'N' and grid[x-1,y+1] == '.' and grid[x-1,y] == '.' and grid[x-1,y-1] == '.':
        return True
    elif d == 'S' and grid[x+1,y-1] == '.' and grid[x+1,y] == '.' and grid[x+1, y+1] == '.':
        return True
    elif d == 'W' and grid[x-1,y-1] == '.' and grid[x,y-1] == '.' and grid[x+1,y-1] == '.':
        return True
    elif d == 'E' and grid[x-1,y+1] == '.' and grid[x,y+1] == '.' and grid[x+1,y+1] == '.':
        return True
    return False

content = [line.replace("\n","") for line in open("day23.txt", encoding="utf8").readlines()]
nrows = len(content)
rowLength = max(len(line) for line in content)

gridSize = 100
padding = (gridSize-rowLength)//2
grid = np.full((gridSize, gridSize), '.', dtype=str)

#populate grid
for i, line in enumerate(content):
    for j, char in enumerate(line):
        grid[i+padding, j+padding] = char

steps = ['N','S','W','E']
moveStepCnt = len(steps)

for k in range(10):
    proposedPositions = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i,j] == '#':
                if allNeighboursEmpty(grid, i, j):
                    continue
                for t in range(4):
                    step = steps[(moveStepCnt+t) % len(steps)]
                    if canMove(grid, i, j, step):
                        if step == 'N': proposedPositions[(i,j)] = (i-1,j)
                        if step == 'S': proposedPositions[(i,j)] = (i+1,j)
                        if step == 'W': proposedPositions[(i,j)] = (i,j-1)
                        if step == 'E': proposedPositions[(i,j)] = (i,j+1)
                        break

    value_count = defaultdict(int)
    for value in proposedPositions.values():
        value_count[value] += 1

    for key, value in proposedPositions.items():
        if value_count[value] == 1:
            old_i, old_j = key
            new_i, new_j = value
            grid[new_i,new_j] = '#'
            grid[old_i,old_j] = '.'

    moveStepCnt += 1

indices = np.argwhere(grid == '#')
min_row, min_col = indices.min(axis=0)
max_row, max_col = indices.max(axis=0)
subgrid = grid[min_row:max_row + 1, min_col:max_col + 1]

print(len(np.argwhere(subgrid == '.')))

