# Otworzenie pliku instrukcje

Podzielenie pliku na linijki i przeniesienie danych do tabeli.
Wyrzucenie ostatniej linijki ponieważ cke nie potrafi formatować plików. 
Stworzenie tablicy dwu wymiarowej gdzie **f[i][0]** to instruckja a **f[i][1]** to parametr.

```python
f = open("instrukcje.txt", "r").read()
f = f.split("\n")
f.pop(-1)
for i in range(len(f)):
    f[i] = f[i].split(" ")
```

Funkcja przesuwająca do następnej litery w alfabecie.
```python
def przAlf(litera):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if alfabet.index(litera) == 25:
        return "A"
    return alfabet[alfabet.index(litera)+1]
```

# Zadanie 4.1 
Pentla for przechodzi przez wszystkie elementy tablicy i sprawdza jakie jest to polecenie.
* Jeżeli polecenie to **"DOPISZ"** korzystając z wbudowanej funkcji *append* dodaje litere z podaną w **f[i][1]** do tablicy napis
* Jeżeli polecenie to **"ZMIEN"** ostatnia litera z zmmiennej napis zostaje zmieniona na litere podaną w **f[i][1]**
* Jeżeli polecenie to **"USUN"** korzystając z wbudowanej funkcji *pop* usuwamy ostatni element tablicy
* Jeżeli polecenie to **"PRZESUN"** to szukamy w zmiennej napis litery podanej w **f[i][1]** wbudowaną fukcją *index* która wyszukuje pierwszej pasującej litery patrząc od lewej i przypisujemy pozycje do zmiennej *indexNapis*. Na podstawie zmiennej *indexNapis* deklarujemy w zmiennej napis na pozycji *indexNapis* litere po przesunięciu wcześniej zadeklarowaną funkcją *przAlf*
```python
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
```
> ## Odpowiedz: 517

---
# Zadanie 4.2
 Pentla for (Przechodząca od 1, do długości *f*) przechodzi przez wszystkie elementy tablicy i czy poprzedni element tablicy jest taki sam jak aktualny.
 * Jeśli tak to dodaje do zmiennej *licznik* 1 
 * Jeżeli nie to sprawdza czy licznik jest większy od nawiększego aktualnego ciągu zapisanego w zmiennej *najCiagInstr*. Jeżeli jest to przypisuje licznik do zmiennej *najCiagInstr* index [1] przypisuje poprzednią instrukcje do *najCiagInstr* index [1] i ustawia licznik na 1.
```python
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
```
> ## Odpowiedz: 517
---

# Stworzenie pliku wynik4.txt.
Stylowanie odpowiedzi do wypisu.
```python
wynik = open("wynik4.txt", "w")

odp1 = "Wynik do zadania 4.1: " + Zadanie1(f)
odp2 = "Wynik do zadania 4.2: " + Zadanie2(f)

wynik.write(odp1)
wynik.write("\n")
wynik.write(odp2)
```