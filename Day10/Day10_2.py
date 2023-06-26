content = open("day10.txt", encoding="utf8").readlines()
cycle, spriteMiddleIndex, CRTindex, CRTrow = 1, 1, 0, ''

def calculateAndDrawCRT(index, row, spriteI):
    if index == spriteI or index == spriteI - 1 or index == spriteI + 1:
        row += '#'
        index += 1
    else:
        row += '.'
        index += 1
    if len(row) == 40:
        print(row)
        row = ''
        index = 0
    return index, row

for line in content:
    line = line.replace('\n','')
    if line.startswith('noop'):
        cycle += 1
        CRTindex, CRTrow = calculateAndDrawCRT(CRTindex, CRTrow, spriteMiddleIndex)
    if line.startswith('addx'):
        command, number = line.split(' ')
        cycle += 1
        CRTindex, CRTrow = calculateAndDrawCRT(CRTindex, CRTrow, spriteMiddleIndex)
        cycle += 1
        CRTindex, CRTrow = calculateAndDrawCRT(CRTindex, CRTrow, spriteMiddleIndex)
        spriteMiddleIndex += int(number)