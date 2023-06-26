import numpy as np
from collections import deque

#bfs algoritem - preverimo če pridemo do zunanjega roba
def seenFromOutside(x,y,z,c):
    queue = deque()
    queue.append((x, y, z))
    visited = set()

    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        if x < 0 or x > 24 or y < 0 or y > 24 or z < 0 or z > 24:
            return True
        if c[x,y,z] == '#':
            continue
        for dx, dy, dz in neigbourCoordinates:
            queue.append((x+dx, y+dy, z+dz))
    return False

#kocko napolnemo s pikami
content = [line.replace("\n", "") for line in open("day18.txt", encoding="utf8").readlines()]
cube = np.full((25, 25, 25), '.', dtype=str)
neigbourCoordinates = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

#nastavimo dobljene koordinate iz inputa kot #
for line in content:
    x, y, z = map(int, line.split(','))
    cube[x,y,z] = '#'

exposed_sides = 0

for x in range(25):
    for y in range(25):
        for z in range(25):
            if cube[x, y, z] == '#':
                for dx,dy,dz in neigbourCoordinates:
                    #preverimo če pridemo do zunanjega roba
                    if seenFromOutside(x+dx,y+dy,z+dz,cube): exposed_sides += 1

print(exposed_sides)
