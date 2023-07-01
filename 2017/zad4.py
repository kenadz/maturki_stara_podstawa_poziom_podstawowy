from math import *

f = open("liczby.txt", "r")

dane = []
for i in range(1000):
    trojka = f.readline().split(" ")
    for j in range(3):
        trojka[j] = int(trojka[j])
    dane.append(trojka)

f.close()

# zad 1
ilosc = 0
for trojka in dane:
    if trojka[0] < trojka[1] < trojka[2]:
        ilosc += 1

print(ilosc)

# print(gcd(123, 54))
# gcd(gdc(a,b), c)

# zad 2
suma_nwd = 0
for trojka in dane:
    nwd = gcd(gcd(trojka[0], trojka[1]), trojka[2])
    suma_nwd += nwd

print(suma_nwd)

# zad 3
ilosc_wierszy = 0
najw_suma = 0
najw_suma_wiersze = 0

for trojka in dane:
    suma = 0
    while trojka[0] > 0:
        suma += trojka[0] % 10
        trojka[0] //= 10
    while trojka[1] > 0:
        suma += trojka[1] % 10
        trojka[1] //= 10
    while trojka[2] > 0:
        suma += trojka[2] % 10
        trojka[2] //= 10

    if suma == 35:
        ilosc_wierszy += 1

    if suma > najw_suma:
        najw_suma = suma
        najw_suma_wiersze = 1
    elif suma == najw_suma:
        najw_suma_wiersze += 1

print(ilosc_wierszy)
print(najw_suma)
print(najw_suma_wiersze)

f = open("wyniki4.txt", "w")

f.write(f"zad 1 {ilosc}\n")
f.write(f"zad 2 {suma_nwd}\n")
f.write(f"zad 3 \nLiczba wierszy o sumie cyfr 35: {ilosc_wierszy} \nNajwiększa suma cyfr: {najw_suma} \nIlość wierszy z największą sumą {najw_suma_wiersze}")

f.close()

