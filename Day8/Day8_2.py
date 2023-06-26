content = open("day8.txt", encoding="utf8").readlines()
treeGrid, highestTreeScore= [], 0

#matrika seznamov podatkov
for line in content:
    treeGrid.append(list(line.replace('\n', '')))

#iteriramo skozi ostala drevesa
for i in range(len(treeGrid[0])):
    for j in range(len(treeGrid)):
        if i != 0 and i != len(treeGrid)-1 and j != 0 and j != len(treeGrid[0])-1:
            treeHeight = int(treeGrid[i][j])

            treeRow = treeGrid[i].copy()
            treeRowLeft = treeRow[:j]
            treeRowRight = treeRow[j+1:]

            treeColumn = []
            for k in range(len(treeGrid)):
                treeColumn.append(treeGrid[k][j])
            treeColumnTop = treeColumn[:i]
            treeColumnBottom = treeColumn[i+1:]

            scenicLeftCount, scenicRightCount, scenicTopCount, scenicDownCount = 0, 0, 0, 0

            for e in reversed(treeRowLeft):
                scenicLeftCount += 1
                if int(e) >= treeHeight:
                    break
            for e in treeRowRight:
                scenicRightCount += 1
                if int(e) >= treeHeight:
                    break
            for e in reversed(treeColumnTop):
                if int(e) >= treeHeight:
                    scenicTopCount += 1
                    break
                scenicTopCount += 1
            for e in treeColumnBottom:
                scenicDownCount += 1
                if int(e) >= treeHeight:
                    break

            score = scenicLeftCount * scenicRightCount * scenicTopCount * scenicDownCount
            if score > highestTreeScore:
                highestTreeScore = score

print(highestTreeScore)