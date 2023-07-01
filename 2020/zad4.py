f = open("liczby.txt", "r")

lista = []

for i in range(1000):
    lista.append(int(f.readline()))

f.close()

print(lista)

# zad 1
ilosc_nieparzystych = 0
for liczba in lista:
    if liczba % 2 == 1:
        ilosc_nieparzystych += 1

# zad 2
podzielne_11 = []
for liczba in lista:
    suma_cyfr = 0
    liczba_kopia = liczba
    while liczba_kopia > 0:
        suma_cyfr += liczba_kopia % 10
        liczba_kopia //= 10
    if suma_cyfr == 11:
        podzielne_11.append(liczba)

# zad 3
pierwsze = []
for liczba in lista:
    pierwsza = True
    if liczba < 2:
        print("Nie jest liczbą pierwszą")
    else:
        for i in range(2, liczba // 2 + 1):
            if liczba % i == 0:
                pierwsza = False
                break
    if liczba >= 4000 and liczba <= 5000 and pierwsza:
        pierwsze.append(liczba)

f = open("wyniki4.txt", "w")
f.write(f"4.1. {ilosc_nieparzystych}\n")
f.write("4.2\n")
for liczba in podzielne_11:
    f.write(str(liczba) + "\n")
f.write(f"4.3\n")
for liczba in pierwsze:
    f.write(str(liczba) + "\n")


f.close()




