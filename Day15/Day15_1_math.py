content = open("day15.txt", encoding="utf8").readlines()
B = []
S = []

for line in content:
    SX, SY, BX, BY = line.replace('Sensor at x=','').replace(', y=','|').replace(': closest beacon is at x=','|').replace(', y=1','|').replace('\n','').split('|')
    S.append((int(SX),int(SY)))
    B.append((int(BX),int(BY)))

def ManhattanDistance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

distances = {}
for i in range(len(S)):
    sensor = S[i]
    beacon = B[i]
    distance = ManhattanDistance(sensor,beacon)
    distances[sensor] = distance

YLineIntervals = {}
for i in range(len(S)):
    sensor = S[i]
    beacon = B[i]
    YLineDX = distances[sensor] - abs(sensor[1]-2000000)
    YLineIntervals[sensor] = (sensor[0] - YLineDX, sensor[0] + YLineDX)

minX = min(v[0] for v in YLineIntervals.values())
maxX = max(v[1] for v in YLineIntervals.values())

countBlocked = -1
for i in range(minX,maxX+1):
    for v in YLineIntervals.values():
        if v[0] <= i <= v[1]:
            countBlocked += 1
            break
print(countBlocked)

