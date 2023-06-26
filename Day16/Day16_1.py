import sys
from functools import cache

@cache
def solve(pos, time, opened):
    if time == 0:
        return 0

    #hoja po valvih in iščemo največji score
    score = max(solve(n, time - 1, opened) for n in maps[pos])

    #če je flow rate večji od 0 potem ima smisel da ga odpremo
    if flows[pos] > 0 and pos not in opened:
        #pretvorimo v navadni set ker frozenset ne dovoli dodajanja
        new_opened = set(opened)
        new_opened.add(pos)

        #zmnožimo preostali čas in flow rate ter rekurzivno kličemo preostale minute. Vrnemo max score
        score = max(score, (time - 1) * flows[pos] + solve(pos, time - 1, frozenset(new_opened)))
    return score

content = [line.replace("\n","") for line in open("day16.txt", encoding="utf8").readlines()]
flows = {}
maps = {}

#parsanje podatkov
for line in content:
    splittedLine = line.split(" ")
    valve = splittedLine[1]
    flows[valve] = int(splittedLine[4].split("=")[1].strip(";"))
    maps[valve] = [t.strip(',') for t in splittedLine[9:]]

print(solve('AA', 30, frozenset()))