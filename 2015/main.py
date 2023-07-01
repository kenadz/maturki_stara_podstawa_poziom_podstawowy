f = open("slowa.txt", "r")

slowa = []
for i in range(999):
    slowa.append(f.readline()[:-1])

slowa.append(f.readline())

f.close()



#print(slowa)

# 5.1

dlugosci = []
for i in range(12):
    dlugosci.append(0)

for slowo in slowa:
    dlugosci[len(slowo) - 1] += 1


# 5.2
# do 5.2 zadania trzeba wczytać drugi plik nowe.txt
f = open("nowe.txt", "r")
nowe = []
for i in range(25):
    nowe.append(f.readline()[:-1])

wystapienia = []
wystapienia_odbicie = []

for i in range(25):
    wystapienia.append(0)
    wystapienia_odbicie.append(0)


for i, slowo_nowe in enumerate(nowe):
    for slowo in slowa:
        if slowo == slowo_nowe:
            wystapienia[i] += 1

        if slowo == slowo_nowe[::-1]:
            wystapienia_odbicie[i] += 1


f = open('wynik5.txt', 'w')

f.write('5.1 \n')
for i, ile in enumerate(dlugosci):
    f.write(f"{i + 1} {ile}\n")
f.write('5.2 \n')
for i in range(25):
    f.write(f"{nowe[i]} {wystapienia[i]} {wystapienia_odbicie[i]} \n")

f.close()
