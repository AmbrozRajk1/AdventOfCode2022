content = open("day8.txt", encoding="utf8").readlines()
treeGrid, visbileTreesCount = [], 0

#matrika seznamov podatkov
for line in content:
    treeGrid.append(list(line.replace('\n', '')))

#preštejemo robna drevesa ki so avtomatsko vidna
visbileTreesCount = len(treeGrid[0]) * 2 + len(treeGrid) * 2 - 4

#pregledamo še ostala drevesa, ki niso na robu ali so vidna s kakšne strani
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

            leftExistsHigher, rightExistsHigher, topExistsHigher, botExistsHigher = False, False, False, False

            #če najdemo kakšno drevo, ki manjše od tega na katerem smo (vse smeri) potem vrne True drugače False
            leftExistsHigher = any(next((x for x in reversed(treeRowLeft) if int(x) >= treeHeight), [False]))
            rightExistsHigher = any(next((x for x in treeRowRight if int(x) >= treeHeight), [False]))
            topExistsHigher = any(next((x for x in reversed(treeColumnTop) if int(x) >= treeHeight), [False]))
            botExistsHigher = any(next((x for x in treeColumnBottom if int(x) >= treeHeight), [False]))

            #če je drevo vidno ga preštejmo
            if leftExistsHigher == False or rightExistsHigher == False or topExistsHigher == False or botExistsHigher == False:
                visbileTreesCount += 1

print(visbileTreesCount)