f = open("dane4.txt", "r")

liczby = []
for i in range(2000):
    liczby.append(int(f.readline()))

f.close()

# zad 1
ilosc_pierwszych = 0
for liczba in liczby:
    pierwsza = True
    for i in range(2, liczba // 2 + 1):
        if liczba % i == 0:
            pierwsza = False
            break

    if pierwsza and liczba > 1:
        ilosc_pierwszych += 1

print(ilosc_pierwszych)

# zad 2
najwieksza = 0
najmniejsza = 30000

for liczba in liczby:
    pierwsza = True
    for i in range(2, liczba // 2 + 1):
        if liczba % i == 0:
            pierwsza = False
            break

    if pierwsza and liczba > 1:
        if liczba < najmniejsza:
            najmniejsza = liczba
        if liczba > najwieksza:
            najwieksza = liczba

print(najmniejsza)
print(najwieksza)

# zad 3

