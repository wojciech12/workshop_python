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

test = 1 + ".Hello"
print(test)
# powyższe polecenie wywoła błąd, czy wiesz dlaczego?

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

# TBD...
