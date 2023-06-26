f = open("day2.txt", encoding="utf8")
content = f.readlines()
score = 0

for line in content:
    first, last = line.split(' ')
    last = last.replace('\n','')
    if first == 'A': #rock
        if last == 'Y': #DRAW
            score = score + 3 + 1
        elif last == 'X': #LOSE
            score = score + 0 + 3
        elif last == 'Z': #WIN
            score = score + 6 + 2
    elif first == 'B': #paper
        if last == 'Y':  # DRAW
            score = score + 3 + 2
        elif last == 'X':  # LOSE
            score = score + 0 + 1
        elif last == 'Z':  # WIN
            score = score + 6 + 3
    elif first == 'C': #scissors
        if last == 'Y':  # DRAW
            score = score + 3 + 3
        elif last == 'X':  # LOSE
            score = score + 0 + 2
        elif last == 'Z':  # WIN
            score = score + 6 + 1

print(score)

