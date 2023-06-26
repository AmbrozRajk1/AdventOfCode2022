content = open("day6.txt", encoding="utf8").readlines()
for i in range(len(content[0])):
    if len(content[0][i:i+4]) == len(set(content[0][i:i+4])):
        print(i+4)
        break