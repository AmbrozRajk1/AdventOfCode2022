f = open("day3.txt", encoding="utf8")
content = f.readlines()
upperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
total = 0

for line in content:
    firstPart = line[:len(line)//2]
    secondPart = line[len(line)//2:]
    for char in firstPart:
        if char in secondPart:
            for i, charFromList in enumerate(upperAlphabet):
                if (charFromList == char):
                    total = total + i + 1 + 26
            for i, charFromList in enumerate(lowerAlphabet):
                if (charFromList == char):
                    total = total + i + 1
            break

print(total)