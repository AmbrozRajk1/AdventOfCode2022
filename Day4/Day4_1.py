f = open("day4.txt", encoding="utf8")
content = f.readlines()
total = 0

for line in content:
    fs, ss = line.replace('\n','').split(',')
    fnfs, snfs = fs.split('-')
    fnss, snss = ss.split('-')

    if ((int(fnfs) >= int(fnss) and int(snfs) <= int(snss)) or (int(fnss) >= int(fnfs) and int(snss) <= int(snfs))):
        total += 1

print(len(content)-total)