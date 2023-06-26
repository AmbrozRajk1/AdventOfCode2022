import json
f = open("day13.txt", encoding="utf8")
content = f.read().split('\n\n')
results = []

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

    #rezultat compare funkcije zapišemo v results
    results.append(compare(p1l,p2l))

#sprehodimo se čez rezultate in preštjemo indexe samo tistega, ki je manjši od 0 (kar pomeni da je prvi element manjši od drugega in sta v pravem vrstnem redu)
totalSum = 0
for i, e in enumerate(results):
    if e < 0:
        totalSum += i+1

print(totalSum)