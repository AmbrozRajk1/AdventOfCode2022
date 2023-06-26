content = open("day10.txt", encoding="utf8").readlines()
cycle = 1
x = 1
signalStrength = 0

def checkCycleAndSignalStrength(c, ss, x1):
    if c == 20 or c == 60 or c == 100 or c == 140 or c == 180 or c == 220:
        ss += c * x1
    return ss

for line in content:
    line = line.replace('\n','')
    if line.startswith('noop'):
        cycle += 1
        signalStrength = checkCycleAndSignalStrength(cycle, signalStrength, x)
    if line.startswith('addx'):
        command, number = line.split(' ')
        cycle += 1
        signalStrength = checkCycleAndSignalStrength(cycle, signalStrength, x)
        cycle += 1
        x += int(number)
        signalStrength = checkCycleAndSignalStrength(cycle, signalStrength, x)
print(signalStrength)