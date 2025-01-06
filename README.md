# Projekt: Linki Śledzące

Projekt służy do rozwiązywania i analizowania linków zawartych w plikach tekstowych, automatycznie sprawdzając, do jakich stron internetowych prowadżą. Skrypt przetwarza plik wejściowy, rozwiązuje linki (w tym obsługuje przekierowania) i zapisuje wynik do nowego pliku z adnotacjami.

## Spis treści

- [Opis](#opis)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Zaawansowane funkcje](#zaawansowane-funkcje)
- [Contributing](#contributing)
- [Licencja](#licencja)

---

## Opis

Skrypt w Pythonie umożliwia:
1. Pobieranie i analizowanie linków zawartych w pliku tekstowym.
2. Obsługę linków z przekierowaniami, np. `https://lnkd.in/...`.
3. Zapisanie wyników w pliku wyjściowym:
   - Rozwiązane linki (z pełnym adresem URL).
   - Linki nierozwiązane z adnotacją `Nierozwiązane`.
   - Linie bez URL z adnotacją `Brak URL`.

Skrypt obsługuje dużą liczbę linków, co czyni go przydatnym w analizach OSINT i pracy z dużymi zbiorami danych.

---

## Wymagania

Do uruchomienia projektu potrzebujesz:
- Python 3.x
- Biblioteki Python:
  - `requests`
  - `urllib3`
  - `re`
  - `logging`

---

## Instalacja

1. **Klonowanie repozytorium**  
   Pobierz projekt z GitHub:

   ```bash
   git clone https://github.com/radektv/linki-sledzace.git
   cd linki-sledzace
   ```

2. **Instalacja zależności**  
   Wykonaj poniższe polecenie w terminalu, aby zainstalować wymagane biblioteki:

   ```bash
   pip install requests
   ```

3. **Przygotowanie plików**  
   - Utwórz plik `linki-sledzace.txt` z linkami do analizy.
   - Opcjonalnie możesz przygotować plik `proxy-free.txt` z adresami proxy w formacie:
     ```plaintext
     proxy1:port
     proxy2:port
     ```

---

## Użycie

1. **Przygotowanie pliku wejściowego**  
   W pliku `linki-sledzace.txt` umieść linki (mogą być wplecione w tekst). Przykład:

   ```plaintext
   1. MetaOSINT: https://lnkd.in/dhX755tY
   2. Bellingcat’s Online Toolkit: https://lnkd.in/e6Q3w5Fk
   3. OSINT Framework: https://lnkd.in/dUyVYSZz
   ```

2. **Uruchomienie skryptu**  
   Aby uruchomić skrypt, wykonaj w terminalu:

   ```bash
   python3 resolve_links.py
   ```

3. **Wynik**  
   Skrypt utworzy plik `wyniki-linki-sledzace.txt` z rozwiązanymi linkami w formacie:

   ```plaintext
   1. MetaOSINT: https://lnkd.in/dhX755tY -> https://metaosint.github.io/
   2. Bellingcat’s Online Toolkit: https://lnkd.in/e6Q3w5Fk -> https://bellingcat.gitbook.io/toolkit
   3. OSINT Framework: https://lnkd.in/dUyVYSZz -> https://osintframework.com/
   ```

   Linie bez rozwiązanego linku zostaną oznaczone jako `Nierozwiązane`.

---

## Zaawansowane funkcje

- **Obsługa proxy**  
  Jeśli plik `proxy-free.txt` zawiera adresy proxy, skrypt automatycznie wykorzysta je w przypadku problemów z połączeniem.
  
- **Logi**  
  Wszystkie błędy i zdarzenia są zapisywane w pliku `url_resolver.log`. Przydatne przy debugowaniu.

- **Losowe User-Agenty**  
  Skrypt korzysta z dynamicznych User-Agentów, co pozwala ominąć blokady serwerów chroniących się przed automatycznym ruchem.

- **Obsługa przekierowań**  
  Skrypt automatycznie śledzi przekierowania HTTP, zapisując ostateczny adres URL.

---

## Contributing

Jeśli chcesz przyczynić się do rozwoju tego projektu, prosimy o utworzenie pull requesta. Upewnij się, że Twój kod jest zgodny ze stylem kodowania i zawiera odpowiednie testy, jeśli są wymagane.

1. Fork repozytorium.
2. Utwórz nową gałąź (branch).
3. Zrób zmiany w kodzie.
4. Prześlij pull request.

---

## Licencja

Ten projekt jest licencjonowany na podstawie **MIT License.**

