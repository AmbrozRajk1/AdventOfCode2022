from collections import deque
content = open("day12.txt", encoding="utf8").readlines()
grid = []

#preberemo in shranimo v seznam (matrika)
for line in content:
    grid.append(list(line.replace('\n', '')))

#začetno pozicijo nastavimo kot a in končno pozicijo kot z
for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item == "S":
            sx = i
            sy = j
            grid[i][j] = "a"
        if item == "E":
            ex = i
            ey = j
            grid[i][j] = "z"

#definiramo vrsto in vanjo dodamo začetno koordinato
q = deque()
q.append((0, ex, ey))

visited = {(ex, ey)}

#dijkstra
while q:
    distance, x1, y1 = q.popleft()
    for x2, y2 in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
        if x2 < 0 or y2 < 0 or x2 >= len(grid) or y2 >= len(grid[0]):
            continue
        if (x2, y2) in visited:
            continue
        if ord(grid[x2][y2]) - ord(grid[x1][y1]) < -1:
            continue
        if grid[x2][y2] == "a":
            print(distance + 1)
            exit(0)
        visited.add((x2, y2))
        q.append((distance + 1, x2, y2))