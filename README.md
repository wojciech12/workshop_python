# Python Workshops

## Wymagania

Proszę przed przyjściem na warsztaty upewnić się, że Twój laptop jest przygotowany. Jeśli są jakieś problemy, proszę użyć kanału slack TBA.

1. Laptop:

   - Rekomendowany: Ubuntu 20.04 lub wirtualna maszyna z Ubuntu 20.04 na [VirtualBoxie](https://www.virtualbox.org/wiki/Downloads)
   - Windows 10 with Python installed

   Rekomendacja wynika z faktu, że programowanie na Linuxie jest łatwiejsze i bez niespodzianek, że jakaś biblioteka nie działa.

   Zainstalowanie VirtualBox jest bardzo proste i jest dużo tutoriali online, które pokazują jak to zrobić.

2. Python3

3. Edytor:

   - [atom](https://atom.io)
   - [vscode](https://code.visualstudio.com)

   lub [PyCharm](https://www.jetbrains.com/pycharm/).

Jeśli będą jakieś problemy ze środowiskiem na początku możemy również skorzystać z [repl.it](https://repl.it/).

## Weryfikacja środowiska

Poniżej kilka kroków które pozwolą się upewnić, że wszystko jest gotowe do warsztatów.

### Czy Python zainstalowany?

Proszę zweryfikować swoje środowisko:

1. Utwórz plik main.py:

   ```
   print("Hello Natalia!")
   ```

   W konsoli lub terminalu uruchom:

   ```
   $ python main.py
   # powinnaś/powinieneś zobaczyć:
   Hello Natalia
   ```

### Czy możemy instalować pakiety?
Utwórz hermetyczne środowisko dla instalacji pakietów.

#### Linux

```
$ python3 -m venv venv
$ source venv/bin/activate
# powinnaś zobaczyć:
(venv)$ pip install requests
```

jeśli nie może znaleźć venv:

```
sudo apt-get update
sudo apt-get install python3-venv
```

#### Windows

W terminalu Windowsa:

```
$ >python -m venv %systemdrive%%homepath%\my-venv
# aktywuj hermetyczne środowisko
# dla bibliotek
$ > %systemdrive%%homepath%\my-venv\Scripts\activate.bat
# zainstaluj bibliotekę pythona
$ pip install requests
```

## Szkolenia

1. [Podstawy 1,2,3](01_podstawy/)
2. Aplikacje webowe z flask - TBA
3. Testowanie aplikacji Python
4. Python i testowanie BDD z Behave aplikacji typu REST
5. [Python i bazy SQL](03_sql/main.pdf)
6. Django
7. notebook jupyter i ML
8. Python i Docker - tylko na Linuxie
9. Python, Docker i Kubernetes
10. Python i Selenium
11. Automatyzacja zasobów chmurowych z Ansible
