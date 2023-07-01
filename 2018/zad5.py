f = open("liczby.txt", "r")

liczby = []

for i in range(1000):
    liczba = f.readline()
    liczby.append(int(liczba))

f.close()

# zad 1
najwieksza = 0
for liczba in liczby:
    if liczba % 2 == 0 and liczba > najwieksza:
        najwieksza = liczba

print(najwieksza)

# zad 2
palindromy = []
for liczba in liczby:
    if str(liczba) == str(liczba)[::-1]:
        palindromy.append(liczba)

print(palindromy)

# zad 3
wieksze_30 = []
suma_wszystkich = 0
for liczba in liczby:
    suma = 0
    kopia = liczba
    while kopia > 0:
        suma += kopia % 10
        kopia = kopia // 10
    if suma > 30:
        wieksze_30.append(liczba)
    suma_wszystkich += suma

f = open("wyniki5.txt", "w")
f.write(f"zad 1 {najwieksza}\n")
f.write("\nzad 2\n")
for liczba in palindromy:
    f.write(str(liczba) + "\n")
f.write("\nzad 3\n")
for liczba in wieksze_30:
    f.write(str(liczba) + "\n")
f.write(f"suma wszystkich cyfr {suma_wszystkich}")

