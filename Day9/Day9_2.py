content = open("day9.txt", encoding="utf8").readlines()
HX, HY = 0, 0
listOfTailCoordinates = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
listOfVisitedTailCoordinates = set()

def getNextCoordinates(headCoordinates, tailCoordinates):
    head_X, head_Y = headCoordinates
    tail_X, tail_Y = tailCoordinates

    #tail right
    if head_X - tail_X > 1 and head_Y == tail_Y: tail_X += 1
    elif head_X - tail_X > 1 and head_Y < tail_Y: tail_X += 1; tail_Y -= 1
    elif head_X - tail_X > 1 and head_Y > tail_Y: tail_X += 1; tail_Y += 1

    #tail left
    elif head_X - tail_X < -1 and head_Y == tail_Y: tail_X -= 1
    elif head_X - tail_X < -1 and head_Y < tail_Y: tail_X -= 1; tail_Y -= 1
    elif head_X - tail_X < -1 and head_Y > tail_Y: tail_X -= 1; tail_Y += 1

    #tail down
    elif head_Y - tail_Y < -1 and head_X == tail_X: tail_Y -= 1
    elif head_Y - tail_Y < -1 and head_X < tail_X: tail_Y -= 1; tail_X -= 1
    elif head_Y - tail_Y < -1 and head_X > tail_X: tail_Y -= 1; tail_X += 1

    #tail up
    elif head_Y - tail_Y > 1 and head_X == tail_X: tail_Y += 1
    elif head_Y - tail_Y > 1 and head_X < tail_X: tail_Y += 1; tail_X -= 1
    elif head_Y - tail_Y > 1 and head_X > tail_X: tail_Y += 1; tail_X += 1

    return (tail_X,tail_Y)

for line in content:
    direction, steps = line.replace('\n','').split(' ')

    for i in range(int(steps)):
        if direction == 'R': HX += 1    #move right
        elif direction == 'U': HY += 1  #move up
        elif direction == 'L': HX -= 1  #move left
        elif direction == 'D': HY -= 1  #move down

        for i, tuple in enumerate(listOfTailCoordinates):
            tail_X, tail_Y = tuple[0], tuple[1]
            head_X, head_Y = 999999, 999999

            if i == 0: head_X, head_Y = HX, HY
            else: head_X, head_Y = listOfTailCoordinates[i - 1]

            listOfTailCoordinates[i] = getNextCoordinates((head_X, head_Y), (tail_X, tail_Y))
        listOfVisitedTailCoordinates.add('({},{})'.format(listOfTailCoordinates[-1][0], listOfTailCoordinates[-1][1]))

print(len(listOfVisitedTailCoordinates))