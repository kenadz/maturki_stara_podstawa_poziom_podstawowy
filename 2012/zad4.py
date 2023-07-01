f = open('cyfry.txt', 'r')
cyfry = []

for i in range(1000):
    cyfry.append(int(f.readline()[:-1]))
f.close()


def suma(a):
    s = 0
    while a > 0:
        s += a % 10
        a /= 10
    return s


def czyRosnacy(a):
    a_str = str(a)
    for i in range(len(a_str) - 1):
        if a_str[i] >= a_str[i+1]:
            return False
    return True


# a)
parzyste = 0

najwieksza_suma_liczb = suma(cyfry[0])
najmniejsza_suma_liczb = suma(cyfry[0])
najwieksza_liczba = cyfry[0]
najmniejsza_liczba = cyfry[0]

ciagi_rosnace = []

for liczba in cyfry:
    if liczba % 2 == 0:
        parzyste += 1
# b)
    suma_liczb = suma(liczba)
    if najmniejsza_suma_liczb > suma_liczb:
        najmniejsza_suma_liczb = suma_liczb
        najmniejsza_liczba = liczba

    if najwieksza_suma_liczb < suma_liczb:
        najwieksza_suma_liczb = suma_liczb
        najwieksza_liczba = liczba
# c)
    if czyRosnacy(liczba):
        ciagi_rosnace.append(liczba)



f = open('zadanie4.txt' , 'w')
f.write(f'a){parzyste}\n')
f.write(f'b) najwieksza suma cyfr: {najwieksza_liczba}, najmniejsza suma cyfr: {najmniejsza_liczba}\n')
f.write('c)\n')
for liczba in ciagi_rosnace:
    f.write(f"{liczba} \n")
