content = open("day9.txt", encoding="utf8").readlines()
HX, HY, TX, TY = 0, 0, 0, 0
listOfVisitedTailCoordinates = set()
print('H coordinates: ({},{}), T coordinates: ({},{})'.format(HX,HY,TX,TY))

for line in content:
    direction, steps = line.replace('\n','').split(' ')

    for i in range(int(steps)):
        if direction == 'R': #move right
            HX += 1
            if HX - TX > 1 and HY == TY:
                TX += 1
            elif HX - TX > 1 and HY - TY == 1:
                TX += 1
                TY += 1
            elif HX - TX > 1 and HY - TY == -1:
                TX += 1
                TY -= 1
            listOfVisitedTailCoordinates.add('({},{})'.format(TX,TY))
            print('H coordinates: ({},{}), T coordinates: ({},{})'.format(HX,HY,TX,TY))
        elif direction == 'U': #move up
            HY += 1
            if HY - TY > 1 and HX == TX:
                TY += 1
            elif HY - TY > 1 and HX - TX == 1:
                TY += 1
                TX += 1
            elif HY - TY > 1 and HX - TX == -1:
                TY += 1
                TX -= 1
            listOfVisitedTailCoordinates.add('({},{})'.format(TX, TY))
            print('H coordinates: ({},{}), T coordinates: ({},{})'.format(HX, HY, TX, TY))
        elif direction == 'L': #move left
            HX -= 1
            if HX - TX < -1 and HY == TY:
                TX -= 1
            elif HX - TX < -1 and HY - TY == 1:
                TX -= 1
                TY += 1
            elif HX - TX < -1 and HY - TY == -1:
                TX -= 1
                TY -= 1
            listOfVisitedTailCoordinates.add('({},{})'.format(TX, TY))
            print('H coordinates: ({},{}), T coordinates: ({},{})'.format(HX, HY, TX, TY))
        elif direction == 'D': #move down
            HY -= 1
            if HY - TY < -1 and HX == TX:
                TY -= 1
            elif HY - TY < -1 and HX - TX == 1:
                TY -= 1
                TX += 1
            elif HY - TY < -1 and HX - TX == -1:
                TY -= 1
                TX -= 1
            listOfVisitedTailCoordinates.add('({},{})'.format(TX, TY))
            print('H coordinates: ({},{}), T coordinates: ({},{})'.format(HX, HY, TX, TY))

print(len(listOfVisitedTailCoordinates))