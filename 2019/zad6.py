f = open("dane.txt", "r")

pesele = []
for liczba in range(1000):
    pesel = f.readline()
    pesel = pesel[0:-1]
    pesele.append(pesel)

f.close()

# zad 1
kobiety = 0
mezczyzni = 0
for pesel in pesele:
    if int(pesel[9]) % 2 == 0:
        kobiety += 1
    else:
        mezczyzni += 1

# zad 2
ilosc_listopad = 0
for pesel in pesele:
    if pesel[2:4] == "11" or pesel[2:4] == "31":
        ilosc_listopad += 1

# zad 3
bledne = []
for pesel in pesele:
    suma = int(pesel[0]) + int(pesel[1]) * 3 + int(pesel[2]) * 7 + int(pesel[3]) * 9 + int(pesel[4]) + int(pesel[5]) * 3 + int(pesel[6]) * 7 + int(pesel[7]) * 9 + int(pesel[8]) + int(pesel[9]) * 3 + int(pesel[10])
    if suma % 10 != 0:
        bledne.append(pesel)

f = open("wyniki6.txt", "w")
f.write(f"6.1 \nkobiety {kobiety} \nmezczyzni {mezczyzni}\n")
f.write(f"6.2 {ilosc_listopad}\n")
f.write("6.3\n")
#f.write("\n".join(bledne))
for pesel in bledne:
    f.write(pesel + "\n")


f.close()



