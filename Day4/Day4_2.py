f = open("day4.txt", encoding="utf8")
content = f.readlines()
total = 0

for line in content:
    fs, ss = line.replace('\n','').split(',')
    fnfs, snfs = fs.split('-')
    fnss, snss = ss.split('-')

    if (int(snfs) < int(fnss) or int(snss) < int(fnfs)):
        total += 1

print(len(content)-total)