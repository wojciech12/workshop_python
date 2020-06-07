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

assert lista[-1] == 'Dorota'

lista.append('Ewelina')  # ['Ania', 'Basia', 'Celina', 'Dorota', 'Ewelina']
lista.remove('Basia')  # ['Ania', 'Celina', 'Dorota', 'Ewelina']

print(lista)

assert lista.index("Celina") == 1

# Modyfikowanie listy
lista[1] = "Gosia"

print(len(lista))  # ilosc elementow w liscie

# Operacje na listach
# lista ['Ania', 'Gosia', 'Dorota','Ewelina']

print(lista[:3])  # ['Ania', 'Gosia', 'Dorota'] 
print(lista[2:])  # ['Dorota', 'Ewelina']
print(lista[3:4])  # ['Ewelina']
print(lista[:])   # ['Ania', 'Gosia', 'Dorota', 'Ewelina'] 

# 4. Petla

# Objekt musi byc iteracyjny

# Petla for 

# range
for numer in range(10):
    print(numer)

# ale moze byc tez slowo
for litera in 'ABCDEFGHIJL':
    print(numer)

# Wazna uwaga - indentacja <- wciecia

for element in lista:
    print(element)

a = 0

# Petla while
while a < 10:
    print(a)
    a+=1
else:
    print("Koniec petli")

# 4. Funkcje

# Funkcje nalezy zadeklarowac od slowa def, funkcja przyjmuje parametry i moze (ale nie musi) zwracac wynik

# Funkcja zwraca wynik dodawania (return)

def add(a, b):
    return a + b

test = add(2, 8)  # =10

print(test)

# Funkcja nie zwracajaca zadnego wyniku ale wykonujaca dzialanie

def print_hello(parametr):
    print("Hello " + str(parametr))

print_hello("Natalia!")

# 5. Slowniki (dictionaries), key-value pair

# Typowy slownik

dictionary = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3",
    "key_n": "value_n"
}

# Bardziej rozbudowany slownik moze opisywac dowolny obiekt.
# Slownik moze zawierac takze listy, slowniki, liczby, slowa

# Nauczymy sie korzystac ze slownikow na bazie przykladu 
# Idziemy na zakupy!

# Najpierw wezmiemy torebke, opiszmy zatem jej podstawowe cechy...

torebka = {
    "kolor": "czarny",
    "zawartosc": ["telefon", "kluczyki", "klucze do domu"]
}

portfel = {
        "kolor": "czerwony",
        "ilosc pieniedzy": 150,
    }

# Cwiczenie - "wlozmy" portfel do torebki. 

torebka['portfel'] = portfel

print(torebka)

# Cwiczenie- zaszalejmy na zakupach!
# W celach utrwalenia poprzednich lekcji napiszemy specjalna funkcje do robienia wirtualnych zakupow w sklepie

def zaplac_za_zakupy(obiekt, zakup, wartosc_zakupu):
    ilosc_pieniedzy = obiekt['portfel']['ilosc pieniedzy']
    ilosc_pieniedzy -= wartosc_zakupu

    if ilosc_pieniedzy >= 0:
        obiekt['zawartosc'].append(zakup)
        obiekt['portfel']['ilosc pieniedzy'] = ilosc_pieniedzy
        return obiekt 
    else:
        print("Niewystarczajaca ilosc pieniedzy")
        return obiekt 


torebka = zaplac_za_zakupy(torebka,'szminka', 50) 
torebka = zaplac_za_zakupy(torebka,'perfumy', 50) 
torebka = zaplac_za_zakupy(torebka,'tusz do rzes', 50) 

print(torebka)

torebka = zaplac_za_zakupy(torebka,'kolczyki', 50) 

#6. Praca z bibliotekami

# Mozemy zaimportowac zewnetrzne biblioteki do usprawniania pracy w jezyku Python

# Powiedzmy, ze nasza torebka nie byla zbyt przejrzysta
# W celu poprawienia przejrzystosci uzyjemy zewnetrznej biblioteki pprint

import pprint  # deklarujemy za pomoca import
pprint.pprint(torebka)

from pprint import pprint as p # mozemy tez zaimportowac czesc biblioteki i nadac jej alias - w tym przypadku p

p(torebka)

# Niektore biblioteki nie sa dostepne bezposrednio w programie i nalezy je importowac z sieci poprzez manager instalacji bibliotek python 

# https://pypi.org/project/pip/

# zainstalujemy biblioteke do czytania plikow PDF
# w tym celu otworzymy okno terminala

# pip3 install textract

# Mozesz zapoznac sie z dokumentacja na stronie projektu

# https://textract.readthedocs.io/en/stable/

import textract

text = textract.process('/Users/bt/Documents/GitHub/workshop_python/01_podstawy/01_Podstawy_1/plik.pdf')

# Uzyjemy poprzedniej biblioteki pprint
p(text)

# Srodowisko hermetyczne venv

# pip3 install virtualenv;
# virtualenv --python=/usr/local/bin/python3 .venv;
# source .venv/bin/activate;
