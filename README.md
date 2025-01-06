# Projekt: Linki Sledzace

Projekt służy do rozwiązywania i analizowania linków zawartych w plikach tekstowych, automatycznie sprawdzając, do jakich stron internetowych prowadzą. Skrypt pobiera plik z linkami, rozwiązuje je i zapisuje wynik do nowego pliku.

Potrzebujesz 2 plików:

Plik 1)
`linki-sledzace.txt` - tutaj wrzucasz swoje linki (nawet z tekstem) np:
```bash
1. MetaOSINT: https://lnkd.in/dhX755tY
2. Bellingcat’s Online Toolkit: https://lnkd.in/e6Q3w5Fk
3. OSINT Framework: https://lnkd.in/dUyVYSZz
4. Nixintel Collection: https://lnkd.in/dnUcNnpW
5. Cyber Detective’s Collection: https://lnkd.in/daEi-9MX
6. Arno Reuser’s OSINT Repertorium: https://rr.reuser.biz/
7. AsINT Collection: https://lnkd.in/dCRNqptZ
8. Achirou OSINT Tools: https://lnkd.in/dK5ZJQD8
```

i dostajesz wynik:
```bash
1. MetaOSINT: https://lnkd.in/dhX755tY -> https://metaosint.github.io/
2. Bellingcat’s Online Toolkit: https://lnkd.in/e6Q3w5Fk -> https://bellingcat.gitbook.io/toolkit
3. OSINT Framework: https://lnkd.in/dUyVYSZz -> https://osintframework.com/
4. Nixintel Collection: https://lnkd.in/dnUcNnpW -> https://start.me/p/rx6Qj8/nixintel-s-osint-resource-list
5. Cyber Detective’s Collection: https://lnkd.in/daEi-9MX -> https://github.com/cipher387/osint_stuff_tool_collection
6. Arno Reuser’s OSINT Repertorium: https://rr.reuser.biz/ -> https://rr.reuser.biz/
7. AsINT Collection: https://lnkd.in/dCRNqptZ -> https://start.me/p/b5Aow7/asint_collection
8. Achirou OSINT Tools: https://lnkd.in/dK5ZJQD8 -> https://achirou.com/category/osint/
```

Plik 2) skrypt `resolve_links.py`

Plik 3) - wygenerowany automatycznie plik po użyciu komendy `python3 resolve_links.py`
`wyniki-linki-sledzace.txt` 

## Spis treści

- [Opis](#opis)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Contributing](#contributing)
- [Licencja](#licencja)

## Opis

Skrypt w Pythonie umożliwia automatyczne pobieranie i analizowanie linków zawartych w pliku tekstowym. Dla każdego linku skrypt wykonuje zapytanie HTTP, sprawdzając, do jakiej strony prowadzi. Rozwiązane linki są zapisywane w nowym pliku tekstowym, który zawiera zarówno oryginalny tekst, jak i rozwiązane adresy URL.

Projekt przydaje się w kontekście analizy linków w dużych zbiorach danych, np. w przypadku zbierania materiałów do analiz OSINT.

## Wymagania

- Python 3.x
- Biblioteka `requests` oraz `re`

## Instalacja

Aby zainstalować wymagane zależności, uruchom poniższe polecenie:

1. **Zainstaluj Git** (jeśli jeszcze tego nie zrobiłeś):

   `sudo apt install git`

   `git clone https://github.com/radektv/linki-sledzace.git`

   `cd linki-sledzace`

2. **Zainstaluj wymagane biblioteki**
   
   `pip install requests`


## Użycie

Aby użyć skryptu, wystarczy uruchomić go w terminalu:

Przygotuj plik wejściowy linki-sledzace.txt z linkami do rozwiązania.

Uruchom skrypt:

`python3 resolve_links.py`

Skrypt utworzy plik wynikowy wyniki-linki-sledzace.txt z rozwiązanymi linkami.


## Contributing

Jeśli chcesz przyczynić się do rozwoju tego projektu, prosimy o utworzenie pull requesta. Upewnij się, że Twój kod jest zgodny ze stylem kodowania i zawiera odpowiednie testy, jeśli są wymagane.

1. Fork repozytorium.
2. Utwórz nową gałąź (branch).
3. Zrób zmiany w kodzie.
4. Prześlij pull request.

## Licencja

Ten projekt jest licencjonowany na podstawie **MIT License.**
