def preberi(ime_datoteke):
    zemljevid = open(ime_datoteke, "r")
    slovar = {}
    for i, vrstica in enumerate(zemljevid, start=1):
        temp = [int(i) for i in vrstica.split()]
        for st in temp:
            if min(temp) == temp[0]:
                break
            else:
                temp += [temp.pop(0)]
        slovar[i] = temp
    zemljevid.close()
    return slovar
zemljevid = preberi("zemljevid.txt")

pot = [1, 3, 6, 11, 14, 16, 15]
navodilo = []
for i in range(1, len(pot) - 1):
    temp = zemljevid[pot[i]]
    #print(temp)
    st = (temp.index(pot[i - 1]) - temp.index(pot[i + 1])+1) % len(temp)
    print(st)
    navodilo.append(abs(st))


print(navodilo, "\n[3, 1, 3, 2, 3]")
