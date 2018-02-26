import risar
from random import random, randint
from time import time
from math import sqrt
risar.obnavljaj = True

cas = time()
krogi = []
kx = []
ky = []
mx, my = risar.miska
speed = 5
miskaKrog = risar.krog(mx, my, 30, sirina=5)

for i in range(30):
    barva = risar.barva(randint(0,255), randint(0,255), randint(0,255))
    pos = risar.nakljucne_koordinate()
    if pos[0] < risar.maxX or pos[1] < risar.maxY:
        pos = risar.nakljucne_koordinate()
    else:
        break
    krogi.append((risar.krog(pos[0], pos[1], 10, barva, sirina=2)))
    kx.append(randint(-5, 5))
    ky.append(sqrt(speed ** 2 - kx[i] ** 2))

while True:

    if risar.levo:
        mx, my = risar.miska
        cas = time()

    if not risar.klik:
        mx, my = risar.miska

    miskaKrog.setPos(mx, my)

    for i in range(len(krogi)):
        krog = krogi[i]
        krog.setPos(krog.x() + kx[i], krog.y() + ky[i])

        if risar.klik and sqrt((krog.x() - mx) ** 2 + (krog.y() - my) ** 2) < 45:
            risar.stoj()

        if not (0 < krog.x() < risar.maxX):
            kx[i] = -kx[i]
        if not (0 < krog.y() < risar.maxY):
            ky[i] = -ky[i]

    if abs(cas - time()) >= 20 and risar.klik:
        break
    risar.cakaj(0.02)

risar.stoj()