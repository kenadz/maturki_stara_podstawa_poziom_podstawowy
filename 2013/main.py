f = open('napisy.txt', 'r')
napisy = []
for i in range(1000):
    napisy.append(f.readline()[:-1])

f.close()

parzyste = 0
rowne_01 = 0
same_0 = 0
same_1 = 0

dlugosci = []
for i in range(15):
    dlugosci.append(0)

for napis in napisy:
    if len(napis) % 2 == 0:
        parzyste += 1

    jedynki = napis.count('1')
    zera = napis.count('0')

    if zera == jedynki:
        rowne_01 += 1

    if jedynki == 0:
        same_0 += 1
    if zera == 0:
        same_1 += 1

    dlugosci[len(napis) - 2] += 1

f = open('zadanie4.txt', 'w')
f.write('a)\n')
f.write(f'{parzyste}\n')
f.write('b)\n')
f.write(f'{rowne_01}\n')
f.write('c)\n')
f.write(f'same zera {same_0}\n')
f.write(f'same jedynki {same_1}\n')
f.write('d)\n')
for i, ilosc in enumerate(dlugosci):
    f.write(f'{i + 2}-znakowe {ilosc}\n')

f.close()