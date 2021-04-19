import timeit

def geprimzahlen(liste):
    if 1 in liste:
        liste.remove(1)
    if 0 in liste:
        liste.remove(0)
    primzahl = []
    for zahl in liste:
        opportunities = [x for x in range(2, zahl)]
        #print(zahl)
        check = []
        #opportunities.pop(-1)
        #print(f"Möglichkeiten {opportunities} für Zahl {zahl}")
        for zahl2 in opportunities[:-1]:
            if zahl % zahl2 == 0:
                check.append(True)

        #print(f"{check} für Zahl {zahl}")
        if len(check) < 1:
            primzahl.append(zahl)


    return primzahl

starttime = timeit.default_timer()
liste = [x for x in range(0,100)]
print(geprimzahlen(liste))
print("Laufzeit ist :", timeit.default_timer()-starttime, "ms")
#print(len(divisor(liste)))

