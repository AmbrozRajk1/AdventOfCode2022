import json
f = open("day13.txt", encoding="utf8")
content = f.read().split('\n\n')
results = [[[2]],[[6]]]

#funkcija ki dela primerjave
def compare(l, r):
    #primerjamo levo in desno stran
    match l, r:
        #če ste oba elementa števili potem odštejemo levega od desnega
        case int(), int():
            return l - r
        #če sta oba elementa seznama potem primerjamo element in element -> rekurzivno kličemo compare ker sta obe števili se bo izvedel prejšnji case
        case list(), list():
            for l1, r1 in zip(l, r):
                res = compare(l1, r1)
                if res != 0:
                    return res
            else:
                return len(l) - len(r)
        #če je levi element število in desni seznam potem levo število pretvorimo v seznam in rekurzivno kličemo compare
        case int(), list():
            return compare([l], r)
        # če je desni element število in levi seznam potem levo število pretvorimo v seznam in rekurzivno kličemo compare
        case list(), int():
            return compare(l, [r])

#beremo pare zaporedoma
for line in content:
    pair1, pair2 = line.split('\n')
    p1l = json.loads(pair1)
    p2l = json.loads(pair2)

    #vse vrstice damo v seznam results
    results.append(p1l)
    results.append(p2l)

#naredimo bubble sort vseh vrstic -> v primeru da sta vrstici v napačnem vrstnem redu jih obrnemo (uporabimo funkcijo compare)
for i in range(len(results)):
    for j in range(len(results)):
        if compare(results[i],results[j]) < 0:
            temp = results[i]
            results[i] = results[j]
            results[j] = temp

#najdemo index od elementa [2] in [6] ter jih zmonožimo
i = results.index([[2]])+1
i2 = results.index([[6]])+1
print(i*i2)