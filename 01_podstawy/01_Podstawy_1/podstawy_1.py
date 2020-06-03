# 1. Wprowadzenie do zmiennych i podstawowe typy danych

# Hello World, czyli pierwszy program każdego programisty..

# Polecenie: Napisz program, który wyświetli w "czarnym" oknie zdanie "Hello Natalia!":

print("Hello Natalia!")

# Funkcja print(....) powoduje wyświetlenie zdania w terminalu.

# Czy chciałabyś zmienić imię?
# Może zapiszemy je w formie zmiennej i przywitamy Wiktorię?

imie = "Wiktoria"
print("Hello " + imie)

#Zwroc prosze uwagę jak polaczylismy poprzednie zdanie ze zmiena. Znak + łączy ciągi znaków.

# Jeśli chcesz, możesz zmienić imię na inne.

# Spróbujmy dokonać odczytu Twojego imienia z okna linii poleceń:

print('Podaj swoje imie:')
imie = input()
print("Hello " + imie)

# Bardziej profesjonalnie (formatted string)
print(f"Hello {imie}")

# Brawo, poznałaś już pierwszą zmienną, to już coś ale przejdźmy dalej!

# Typy danych

# * Int -> .., -10 .. 1, 2 .. czyli liczba calkowita
# * Float -> 1.23, 1.333333 .. ulamki
# * Bool -> 0 lub 1, True albo False, punkt widzenia programisty...
# * Str -> 'tekst', "tekst2", """tekst3"""

# 'I am happy!'
# "I'm happy!"
# 'Mój ulubiony film to "Gladiator"'

# """Mój kot ma na imię "Cicik" .. I'm happy....
# Zacznijmy nowe zdanie..."""


# * List -> ['Anna','Barbara','Celina']
# * Tuple -> ('Anna','Barbara','Celina')
# * Dict

# {
#     "imie": "Anna",
#     "nazwisko": "Kowalska",
#     "wiek": 21,
#     "jezyki": ['angielski','polski','niemiecki']
# }

# * Set
# * None

# 2. Podstawowe operacje matematyczne

dodawanie = 1 + 3  # = 4
print(dodawanie)

odejmowanie = 1 - 3  # = -2
print(odejmowanie)

mnozenie = 1 * 3  # = 3
print(mnozenie)

dzielenie = 1 / 3  # = 0.33333333
print(dzielenie)

zaokraglenie = round(1.0 / 3, 2)  # = 0.33
print(zaokraglenie)

modulo = 7 % 3  # = 1
print(modulo)

# Kolejnosc wykonywania operacji - jak w matematyce

print(2 + 3 * 2 - 1) # 3 * 2 -> 2 + 6 -> 8 - 1 -> 7

# Kolejnosc wykonywania operacji cd..

print((2 + 3) * (2 - 1)) # 2 + 3 -> 5 .. 2 - 1 -> 1 .. 5 * 1 -> 5

# Laczenie cyfr i znakow

# powyższe polecenie wywoła błąd, czy wiesz dlaczego?

# test = 1 + ".Hello"
# print(test)

# W celu połączenia numerów i znaków powinniśmy je zadeklarować jako ten sam typ zmiennej:

print(str(1) + ".Hello")

# Operatory

# =
a = 1
print(a)

# ==
a = 1
b = 3

test = (a == b) # False
print(test)

# a > b, a >= b, b <= a, b != a

# operatory inkrementacji <- zwiekszenia

# Rozwazmy przyklad:
a = 1
a = a + 1

print(a)

a = 1
a += 1
print(a)

# -=
# *=
# /=

# assert <- zalozenie, ze

# assert 0 == 1  # Error
assert 1 == 1  # no error

# 3. Listy - modyfikowalne zbiory danych

lista = ['Ania','Basia','Celina', 'Dorota']

assert (lista[0] == 'Ania')  # True

# Slice
print(lista[:4])  # prints from beginning to end index
print(lista[2:])  # prints from start index to end of list
print(lista[2:4]) # prints from start index to end index
print(lista[:])   # prints from beginning to end of list

assert test == 'Dorota'

lista.append('Ewelina')  # ['Ania', 'Basia', 'Celina', 'Dorota', 'Ewelina']
lista.remove('Basia')  # ['Ania', 'Celina', 'Dorota', 'Ewelina']

print(lista)

assert lista.index("Celina") == 1

# Modyfikowanie listy
lista[1] = "Gosia"

print(len(lista))  # ilosc elementow w liscie

