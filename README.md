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
   ```bash
   sudo apt install git
