# Otworzenie pliku instrukcje
f = open("instrukcje.txt", "r").read()

#Podzielenie pliku na linijki i przeniesienie danych do tabeli 
f = f.split("\n")

#Wyrzucenie ostatniej linijki ponieważ cke nie potrafi formatować plików 
f.pop(-1)

#Stworzenie tablicy dwu wymiarowej gdzie f[i][0] to instruckja a f[i][1] to parametr
for i in range(len(f)):
    f[i] = f[i].split(" ")

# Definicja funkcji z przekazaniem pliku w formie tablicy
def Zadanie1(f):
    
    #Funkcja przesuwająca do następnej litery w alfabecie
    def przAlf(litera):
        alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if alfabet.index(litera) == 25:
            return "A"
        return alfabet[alfabet.index(litera)+1]
    
    # Tablica zbierająca wszystkie efekty polecenia
    napis = []
    
    # Pentla for przechodzi przez wszystkie elementy tablicy i sprawdza jakie jest to polecenie
    for i in range(len(f)):

        # Jeżeli polecenie to "DOPISZ" korzystając z wbudowanej funkcji append dodaje litere z podaną w f[i][1] do tablicy napis
        if f[i][0] == "DOPISZ":
            napis.append(f[i][1])

        # Jeżeli polecenie to "ZMIEN" ostatnia litera z zmmiennej napis zostaje zmieniona na litere podaną w f[i][1]
        if f[i][0] == "ZMIEN":
            napis[-1] = f[i][1]

        # Jeżeli polecenie to "USUN" korzystając z wbudowanej funkcji pop usuwamy ostatni element tablicy 
        if f[i][0] == "USUN":
            napis.pop(-1)

        # Jeżeli polecenie to "PRZESUN" to szukamy w zmiennej napis litery podanej w f[i][1] wbudowaną fukcją index która wyszukuje pierwszej pasującej litery patrząc od lewej i przypisujemy pozycje do zmiennej indexNapis. Na podstawie zmiennej indexNapis deklarujemy w zmiennej napis na pozycji indexNapis litere po przesunięciu wcześniej zadeklarowaną funkcją przAlf
        if f[i][0] == "PRZESUN":
            indexNapis = napis.index(f[i][1])
            napis[indexNapis] = przAlf(f[i][1])
    return str(len(napis))




# Stworzenie pliku wynik4.txt
wynik = open("wynik4.txt", "w")

# Stylowanie odpowiedzi do wypisu
odp1 = "Wynik do zadania 4.1: " + Zadanie1(f)

wynik.write(odp1)

