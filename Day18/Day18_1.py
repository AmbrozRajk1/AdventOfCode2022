import numpy as np

#kocko napolnemo s pikami
content = [line.replace("\n","") for line in open("day18.txt", encoding="utf8").readlines()]
cube = np.full((25,25,25), '.', dtype=str)

#nastavimo dobljene koordinate iz inputa kot #
for line in content:
    x, y, z = map(int, line.split(','))
    cube[x,y,z] = '#'

exposed_sides = 0

#zgolj iteriramo po vseh elementih najdemo sosede in preverimo kateri so pika
for x in range(25):
    for y in range(25):
        for z in range(25):
            if cube[x, y, z] == '#':
                neighbors = [
                    cube[x - 1, y, z],
                    cube[x + 1, y, z],
                    cube[x, y - 1, z],
                    cube[x, y + 1, z],
                    cube[x, y, z - 1],
                    cube[x, y, z + 1]
                ]
                exposed_sides += neighbors.count('.')

print(exposed_sides)