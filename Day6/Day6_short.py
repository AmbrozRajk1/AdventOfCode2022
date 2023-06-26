content = open("day6.txt", encoding="utf8").readlines()
[print(i+14) for i in range(len(content[0])) if len(content[0][i:i+14]) == len(set(content[0][i:i+14]))]