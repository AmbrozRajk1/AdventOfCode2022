f = open("day3.txt", encoding="utf8")
content = f.readlines()
upperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
total = 0
index = 0
threeLines = ''

for line in content:
    threeLines += line + "-"
    index += 1

    if(index == 3):
        firstLine, secondLine, thirdLine, ex = threeLines.split('-')
        index = 0
        threeLines = ''
        for char in firstLine:
            if char in secondLine and char in thirdLine:
                for i, charFromList in enumerate(upperAlphabet):
                    if (charFromList == char):
                        total = total + i + 1 + 26
                for i, charFromList in enumerate(lowerAlphabet):
                    if (charFromList == char):
                        total = total + i + 1
                break

print(total)