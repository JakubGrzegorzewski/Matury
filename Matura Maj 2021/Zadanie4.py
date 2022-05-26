f = open("instrukcje.txt", "r").read()
f = f.split("\n")
f.pop(-1)

for i in range(len(f)):
    f[i] = f[i].split(" ")

def przAlf(litera):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if alfabet.index(litera) == 25:
        return "A"
    return alfabet[alfabet.index(litera)+1]

def Zadanie1(f):
    napis = []

    for i in range(len(f)):
        if f[i][0] == "DOPISZ":
            napis.append(f[i][1])

        if f[i][0] == "ZMIEN":
            napis[-1] = f[i][1]

        if f[i][0] == "USUN":
            napis.pop(-1)

        if f[i][0] == "PRZESUN":
            indexNapis = napis.index(f[i][1])
            napis[indexNapis] = przAlf(f[i][1])

    return str(len(napis))


def Zadanie2(f):
    najCiagInstr = ["Dopisz", 0]
    licznik = 1
    
    for i in range(1, len(f)):
        if f[i][0] == f[i-1][0]:
            licznik += 1

        if f[i][0] != f[i-1][0]:
            if licznik > najCiagInstr[1]:
                najCiagInstr[1] = licznik
                najCiagInstr[0] = f[i-1][0]
            licznik = 1

    return " ".join([najCiagInstr[0],str(najCiagInstr[1])])

def Zadanie3(f):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(f)):
        if f[i][0] == "DOPISZ":
            lista[alfabet.index(f[i][1])] += 1
    return alfabet[lista.index(max(lista))] + " " + str(max(lista))

def Zadanie4(f):
    napis = []

    for i in range(len(f)):
        if f[i][0] == "DOPISZ":
            napis.append(f[i][1])

        if f[i][0] == "ZMIEN":
            napis[-1] = f[i][1]

        if f[i][0] == "USUN":
            napis.pop(-1)

        if f[i][0] == "PRZESUN":
            indexNapis = napis.index(f[i][1])
            napis[indexNapis] = przAlf(f[i][1])

    return "".join(napis)


wynik = open("wynik4.txt", "w")

odp1 = "Wynik do zadania 4.1: " + Zadanie1(f)
odp2 = "Wynik do zadania 4.2: " + Zadanie2(f)
odp3 = "Wynik do zadania 4.3: " + Zadanie3(f)
odp4 = "Wynik do zadania 4.4: " + Zadanie4(f)

wynik.write(odp1)
wynik.write("\n")
wynik.write(odp2)
wynik.write("\n")
wynik.write(odp3)
wynik.write("\n")
wynik.write(odp4)

