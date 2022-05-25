# Matura Maj 2021
---
## Zadanie 4
Pewna firma przygotowuje wyświetlanie napisów złożonych z wielkich liter alfabetu angielskiego. Na początku napis jest pusty (nie zawiera liter). W pliku **instrukcje.txt** podanych jest 2000 instrukcji, które wykonuje automat do generowania napisu. Każda z instrukcji składa się z polecenia, spacji oraz pojedynczego znaku. Polecenia są czterech rodzajów: 

* DOPISZ litera – oznacza, że na końcu napisu trzeba dopisać pojedynczą literę; 
* ZMIEN litera – oznacza, że ostatnią literę aktualnego napisu należy zmienić na podaną literę (możesz założyć, że napis jest niepusty); 
* USUN 1 – oznacza, że należy usunąć ostatnią literę aktualnego napisu (możesz założyć, że napis jest niepusty); 
* PRZESUN litera – oznacza, że pierwsze od lewej wystąpienie podanej litery w napisie należy zamienić na następną literę w alfabecie (jeśli litera to A, to należy zamienić na B, jeśli B, to na C itd.) Literę Z należy zamienić na A. Jeśli litera nie występuje w napisie, nie należy nic robić.

> **Przykład:** 
Dany jest następujący ciąg instrukcji: 
DOPISZ A 
DOPISZ B 
DOPISZ C 
USUN 1 
DOPISZ D 
ZMIEN B 
DOPISZ E 
PRZESUN B

Po wykonaniu pierwszych trzech instrukcji napis będzie miał postać ABC, potem AB, ABD, ABB, ABBE, wreszcie ostatnia instrukcja zamieni pierwsze B na C, więc ostatecznie powstały napis to ACBE. Napisz program (lub kilka programów), który(-e) znajdzie(-dą) odpowiedzi na poniższe pytania. Każdą odpowiedź zapisz w pliku wyniki4.txt i poprzedź ją numerem oznaczającym zadanie. Do dyspozycji masz również plik przyklad.txt, w którym znajduje się tylko 20 instrukcji – odpowiedzi dla tego pliku podane są w treściach zadań, możesz więc sprawdzać na nim działanie swojego programu. Pamiętaj, że Twój program musi ostatecznie działać dla 2000 instrukcji.

### Zadanie 4.1
Oblicz całkowitą długość napisu po wykonaniu wszystkich instrukcji z pliku **instrukcje.txt.**
>Dla pliku **przyklad.txt** długością napisu jest liczba 10. 

### Zadanie 4.2
Znajdź najdłuższy ciąg występujących kolejno po sobie instrukcji tego samego rodzaju. Jako odpowiedź podaj rodzaj instrukcji oraz długość tego ciągu. Istnieje tylko jeden taki ciąg. 
>Dla pliku **przyklad.txt** odpowiedzią jest: rodzaj instrukcji – DOPISZ, długość ciągu – 5

### Zadanie 4.3
Oblicz, która litera jest najczęściej dopisywana (najczęściej występuje w instrukcji DOPISZ). Podaj tę literę oraz ile razy jest dopisywana. Istnieje tylko jedna taka litera. 
> Dla pliku **przyklad.txt** odpowiedzią jest litera U, dopisywana 3 razy. 

### Zadanie 4.4
Podaj napis, który powstanie po wykonaniu wszystkich instrukcji z pliku **instrukcje.txt.**
> Dla pliku **przyklad.txt** wynikiem jest napis **ALANTURING.**

### WYNIK MA BYĆ ZAPISANY W PLIKU " **wynik4.txt** "

---

## Zadanie 5

Wodociągi miejskie zamierzają wykonać analizę zużycia wody. W tym celu zgromadziły dane o poborze wody przez wszystkich swoich klientów za rok 2019. Dane są zapisane w pliku **wodociagi.txt**. Pierwszy wiersz pliku jest wierszem nagłówkowym, a dane rozdzielono średnikami. W każdym wierszu zapisano informacje dotyczące gospodarstwa domowego jednego klienta: dziesięcioznakowy kod klienta oraz 12 liczb całkowitych oznaczających ilości zużytej wody w m3 przez kolejnych 12 miesięcy (od stycznia do grudnia). Kod klienta składa się z pięciocyfrowego numeru klienta, dwucyfrowej liczby oznaczającej liczbę osób pozostających we wspólnym gospodarstwie domowym oraz trzyliterowego kodu dzielnicy miasta. Każdy kod jest unikatowy. 

> Fragment pliku **wodociagi.txt**: 
> 
|KodKlienta|I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0000103WIL|6|6|6|9|6|15|12|12|12|6|9|6|
|0000403BEM|6|3|9|9|12|15|15|15|9|6|3|9|

Korzystając z powyższych danych oraz dostępnych narzędzi informatycznych, wykonaj podane zadania. Wyniki zapisz w pliku tekstowym **wyniki5.txt**. Odpowiedź do każdego zadania poprzedź numerem tego zadania.

### Zadanie 5.1

Utwórz zestawienie zawierające **pięciocyfrowe** numery 10 klientów, którzy w ciągu roku zużyli w swoim gospodarstwie domowym średnio najwięcej wody na jedną osobę, oraz ich średnie zużycie wody na jedną osobę. Średnioroczne zużycie wody na jedną osobę zaokrąglij do dwóch miejsc po przecinku. 

Zestawienie, zawierające numery klientów i średnie zużycie wody na jedną osobę, uporządkuj nierosnąco według średniej.

### Zadanie 5.2
Dla każdej dzielnicy podaj całkowite roczne zużycie wody przez jej wszystkich mieszkańców. 

### Zadanie 5.2
Dla każdej dzielnicy oblicz zużycie wody w każdym miesiącu łącznie przez wszystkich mieszkańców tej dzielnicy. Podaj maksymalne miesięczne zużycie wody w każdej z dzielnic. 

### Zadanie 5.3
Dział inwestycji analizuje konieczność modernizacji sieci wodociągowej na podstawie danych za rok 2019. Jako podstawę obliczeń bierze sumaryczne zużycie wody w każdym z 12 miesięcy. Inżynierowie założyli, że sumaryczne miesięczne zużycie wody będzie rosło o 1% rok do roku każdego miesiąca (w m3 z zaokrągleniem w górę do najbliższej liczby całkowitej).

>**Przykład**: 
jeśli w styczniu 2019 roku sumaryczne zużycie wody w mieście wyniosło 53 545 m3, to w styczniu 2020 przewidywane zużycie wyniesie 54 081 m3

**Uwaga:** dla danych z zadania przewidywane zużycie wody w maju 2025 roku wyniesie 90 898 m3.


Obecnie maksymalny miesięczny przepływ (wydajność sieci) wynosi 160 000 m3. Podaj rok i miesiąc, w którym pierwszy raz zabraknie wody w mieście (przewidywane zużycie będzie większe niż maksymalny przepływ sieci). Sporządź zestawienie obrazujące przewidywane zużycie wody w każdym z kolejnych miesięcy od stycznia 2020 roku do grudnia 2030 roku. Narysuj wykres liniowy obrazujący przewidywane zużycie wody w każdym z kolejnych miesięcy w **2030 roku.**

### Zadanie 5.4
Wodociągi miejskie zaplanowały inwestycję, która począwszy od 2021 roku corocznie w styczniu pozwoli na zwiększanie maksymalnego przepływu o 1000 m3. Podaj rok i miesiąc, kiedy pierwszy raz zabraknie wody w mieście po uwzględnieniu tej inwestycji. 

### WYNIK MA BYĆ ZAPISANY W PLIKU " **wynik5.txt** "

---

## Zadanie 6

W internetowej grze Bitwa o Kamienną Bramę bierze udział wielu graczy z całego świata. Każdy gracz może budować różnego rodzaju jednostki (np. robotników, piechurów, łuczników, szpiegów lub magów), które może wykorzystać do budowy wirtualnego księstwa lub wystawić do bitwy. Polem gry jest duża plansza, na której każda jednostka zajmuje pewne miejsce. Każdy gracz może mieć wiele jednostek, np. kilku robotników, drwali, balist i innych. W plikach **gracze.txt, klasy.txt** oraz **jednostki.txt** podano aktualny stan wirtualnej planszy. Dane w tych plikach podane są w kolejnych wierszach, w każdym wierszu pola oddzielono znakiem tabulacji. Pierwszy wiersz każdego z plików jest wierszem nagłówkowym. 
> Plik **gracze.txt** zawiera informację o graczach: 
* unikatowy identyfikator będący liczbą całkowitą, numer gracza (id_gracza) 
* kraj pochodzenia (kraj) 
* datę dołączenia do gry (data_dolaczenia) w formacie rrrr-mm-dd 

| id_gracza | kraj | data_dolaczenia |
| ----------- | ----------- | ----------- |
| 1 | Japonia | 2018-02-15 |
| 2 | Indie | 2017-06-08 |
| 3 | Stany Zjednoczone | 2019-06-10 |

> W pliku **klasy.txt** podano klasy jednostek, jakie gracz może budować. Każda klasa jest opisana przez następujące parametry: 
* nazwę klasy jednostek (nazwa) 
* siłę (sila), strzał (strzal) oraz magię (magia) – trzy atrybuty określające zdolności jednostek tej klasy 
* szybkość (szybkosc) – prędkość poruszania się jednostek tej klasy nazwa sila strzal magia szybkosc 

| nazwa sila | strzal | magia | szybkosc |
| ----------- | ----------- | ----------- | ----------- |
| zwiadowca | 8 | 5 | 0 | 25 |
| lucznik | 5 | 10 | 0 | 12 |
| mag ognia | 5 | 0 | 15 | 10 |
| paladyn | 20 | 0 | 5 | 20 |

> W pliku **jednostki.txt** podano stan planszy, czyli wszystkie jednostki zbudowane przez graczy. Jeden wiersz pliku opisuje jedną jednostkę za pomocą następujących informacji: 
* unikatowy identyfikator będący liczbą naturalną (id_jednostki) 
* identyfikator gracza, do którego należy jednostka (id_gracza) 
* nazwę klasy, do której należy jednostka (nazwa) 
* miejsce jednostki na planszy – jej współrzędne x i y (lok_x, lok_y) 

| id_jednostki | id_gracza | nazwa | lok_x | lok_y | 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 1 | 153 | piechur | 166 | 30 | 
| 2 | 60 | topornik | 36 | 44 | 
| 3 | 88 | drwal | 134|  88 | 
| 4 | 182|  kusznik | 3 | 196 | 

Korzystając z dostępnych narzędzi informatycznych, wykonaj poniższe polecenia. Odpowiedzi 
zapisz w pliku **wyniki6.txt**, a każdy podpunkt poprzedź odpowiadającym mu numerem 
zadania.

### Zadanie 6.1
Podaj 5 krajów, z których najwięcej graczy dołączyło do gry w 2018 roku. Dla każdego z tych krajów podaj liczbę graczy, którzy dołączyli w 2018 roku. 

### Zadanie 6.2
Podaj sumę wartości pola strzał (strzal) dla każdej klasy jednostek, które mają „elf” jako część nazwy.

### Zadanie 6.3
Podaj numery graczy, którzy nie mają artylerzystów (jednostek o nazwie artylerzysta). Numery podaj w porządku rosnącym. 

### Zadanie 6.4
Jeden krok jednostki to przejście o 1 w dowolnym z czterech kierunków (północ, południe, wschód lub zachód). W jednej turze jednostka może wykonać co najwyżej tyle kroków, ile wynosi jej szybkosc. Innymi słowy jednostka w ciągu jednej tury może przemieścić się z punktu (x,y) do punktu (x1,y1), jeśli |x – x1| + |y – y1| ≤ szybkosc. Tytułowa Kamienna Brama znajduje się w miejscu (100,100). Wyszukaj jednostki, które mogą w jednej turze dojść do Bramy, i podziel je na poszczególne klasy. Utwórz zestawienie, które dla każdej klasy poda jej nazwę oraz liczbę jednostek z tej klasy mogących w jednej turze osiągnąć Bramę. 

### Zadanie 6.5
Jeśli w pewnej lokalizacji znajdują się jednostki więcej niż jednego gracza, toczy się tam (jedna) bitwa. Oblicz: 
1. ile bitew ma miejsce na planszy, 
2. w ilu bitwach biorą udział gracze z Polski. 

**Uwaga:** zauważ, że w jednej lokalizacji może się znajdować więcej niż jedna jednostka tego samego gracza.

### WYNIK MA BYĆ ZAPISANY W PLIKU " **wynik6.txt** "

---