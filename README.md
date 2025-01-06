# Projekt: Linki Sledzace

Projekt służy do rozwiązywania i analizowania linków zawartych w plikach tekstowych, automatycznie sprawdzając, do jakich stron internetowych prowadzą. Skrypt pobiera plik z linkami, rozwiązuje je i zapisuje wynik do nowego pliku.

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
- Biblioteka `requests`

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
