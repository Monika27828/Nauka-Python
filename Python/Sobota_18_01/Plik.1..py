# # Bardzo zagnieżdżony słownik
#
# firma = {
#     "Dział IT": {
#         'pracownik_1' : {'imie' : 'Anna', 'wiek' : 27},
#         'pracownik_2' : {'imie' : 'Kasia', 'wiek' : 26}
#     },
#     'Dział HR': {
#         'pracownik_1': {'imie': 'Mateusz', 'wiek': 25},
#         'pracownik_2': {'imie': 'Maciej', 'wiek': 21}
#     },
# }
#
# print(firma['Dział IT']['pracownik_2']['imie'])
#
# for dzial, pracownicy in firma.items():
#     print(f'{dzial}')
#     for id_pracownika, dane in pracownicy.items():
#         print(f'{id_pracownika} : {dane}')
#
# firma['Dział IT']['pracownik_3'] = {'imie' : 'Aleksander', 'wiek' : 29}
#
# print(firma)
#
# del firma['Dzial HR']['pracownik_1']
# print(firma['Dzial HR'])

# Krotki

# krotka1 = (1, 2, 3, 4)
# krotka2 = ('Ala', 'ma', 'kota')
# krotka3 = ()
# krotka4 = (42,)
#
# print(krotka1[0])
# print(krotka2[-1])
#
# a, b, c, d = krotka1
#
# krotka5 = krotka1 + krotka2
# print(krotka5)
#
# krotka6 = ((1,2),(3,4), (5,6))
# print(krotka6[0][1])
#
# for element in krotka2:
#     print(element)
#
# wspolrzedne = {
#     (0,0) : 'Początek',
#     (1,2) : 'A',
#     (4,6) : 'B'
# }
# print(wspolrzedne[(1,2)])
#
# def oblicz_statystyki(lista):
#     suma = sum(lista)
#     srednia = suma / len(lista)
#     minimum = min(lista)
#     maksimum = max(lista)
#     return suma, srednia, minimum, maksimum
# wynik = oblicz_statystyki([1,2,3,4,5])
# print(wynik)
#
# dane = [
#     ('Jan', 30, 4000),
#     ('Anna', 25, 5000),
#     ('Michael', 30, 3000),
# ]
#
# posortowana_krotka = sorted(dane, key = lambda x: x[2])
# print(posortowana_krotka)
#
# def suma(*args):
#     return sum(args)
# print(suma(1,2,3,4,5))

# Zadania do wykonania:
# 1. Napisz funkcję, która przyjmuje listę krotek zawierających dane studentów (imię, nazwisko, średnia ocen)
# i zwraca dane studenta z najwyższą średnią.
# 2. Utwórz słownik, w którym kluczami będą współrzędne (krotki), a wartościami nazwy miast.
# Dodaj kilka przykładów i wyświetl wszystkie miasta.
# 3. Utwórz listę krotek zawierających dane o produktach (nazwa, cena, ilość) i posortuj je według ceny,
# a następnie według ilości malejąco.

# # Ad.1
#
# def the_best_student(students):
#
#     return max(students, key=lambda student: student[2])
#
# students = [
#     ("Jan", "Kowalski", 4.5),
#     ("Anna", "Nowak", 4.8),
#     ("Piotr", "Zieliński", 4.7)
# ]
#
# best = the_best_student(students)
# print(f"The best student: {best[0]} {best[1]}, średnia: {best[2]}")
#
# # Ad.2
#
# cities = {
#     (52.2297, 21.0122): "London",
#     (51.1079, 17.0385): "Glasgow",
#     (50.0647, 19.9450): "Edinburgh",
#     (51.2465, 22.5687): "York"
# }
#
# for coordinates, city in cities.items():
#     print(f"Coordinates: {coordinates}, City: {city}")

# # Ad.3
#
# produkty = [
#     ("Jabłka", 2.5, 100),
#     ("Banan", 1.2, 200),
#     ("Pomarańcze", 3.0, 150),
#     ("Gruszki", 2.5, 50),
#     ("Wiśnie", 4.0, 75)
# ]
#
# # Sortujemy listę najpierw według ceny (rosnąco), a potem według ilości (malejąco)
# produkty_posortowane = sorted(produkty, key=lambda produkt: (produkt[1], -produkt[2]))
#
# # Wyświetlamy posortowaną listę produktów
# for produkt in produkty_posortowane:
#     print(f"Nazwa: {produkt[0]}, Cena: {produkt[1]}, Ilość: {produkt[2]}")

# Funkcje.

# def oblicz_pole_prostokata(a, b):
#     """Oblicza pole prostokąta:
#     Argumenty:
#     a -- długość boku prostokąta
#     b -- szerokość prostokąta
#     """
#     return a * b
# print(oblicz_pole_prostokata(5, 10))
# print(oblicz_pole_prostokata.__doc__)

def funkcja_a(x):
    return x + 10

zmienna_funkcyjna = funkcja_a

print(zmienna_funkcyjna(5))

def funkcja_b(funkcja, liczba):
    return 5 + funkcja(liczba)

wynik = funkcja_b(funkcja_a, 20)
print(wynik)

def funkcja_c(x):
    def funkcja_wewnetrzna(y):
        x + y

    return funkcja_wewnetrzna

nowa_funkcja = funkcja_c(5)
print(nowa_funkcja(10))
