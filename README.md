# Projekt: Linki Śledzące

Projekt służy do rozwiązywania i analizowania linków zawartych w plikach tekstowych, automatycznie sprawdzając, do jakich stron internetowych prowadzą. Skrypt przetwarza plik wejściowy, rozwiązuje linki (w tym obsługuje przekierowania) i zapisuje wynik do nowego pliku z adnotacjami.

---

# Project: Link Resolver

This project is designed to resolve and analyze links contained in text files, automatically checking which websites they lead to. The script processes an input file, resolves links (including handling redirects), and saves the results to a new annotated file.

---

## Spis treści / Table of Contents

- [Opis / Description](#opis--description)
- [Wymagania / Requirements](#wymagania--requirements)
- [Instalacja / Installation](#instalacja--installation)
- [Użycie / Usage](#użycie--usage)
- [Zaawansowane funkcje / Advanced Features](#zaawansowane-funkcje--advanced-features)
- [Contributing](#contributing)
- [Licencja / License](#licencja--license)

---

## Opis / Description

### [PL]
Skrypt w Pythonie umożliwia:
1. Pobieranie i analizowanie linków zawartych w pliku tekstowym.
2. Obsługę linków z przekierowaniami, np. `https://lnkd.in/...`.
3. Zapisanie wyników w pliku wyjściowym:
   - Rozwiązane linki (z pełnym adresem URL).
   - Linki nierozwiązane z adnotacją `Nierozwiązane`.
   - Linie bez URL z adnotacją `Brak URL`.

Skrypt obsługuje dużą liczbę linków, co czyni go przydatnym w analizach OSINT i pracy z dużymi zbiorami danych.

### [EN]
The Python script enables:
1. Extracting and analyzing links from a text file.
2. Handling redirected links, e.g., `https://lnkd.in/...`.
3. Saving results to an output file:
   - Resolved links (with full URLs).
   - Unresolved links annotated as `Unresolved`.
   - Lines without URLs annotated as `No URL`.

The script supports a large number of links, making it useful for OSINT analyses and working with big datasets.

---

## Wymagania / Requirements

- Python 3.x
- Python Libraries:
  - `requests`
  - `urllib3`
  - `re`
  - `logging`

---

## Instalacja / Installation

1. **Klonowanie repozytorium / Clone the repository**

   ```bash
   git clone https://github.com/radektv/linki-sledzace.git
   cd linki-sledzace
   ```

2. **Instalacja zależności / Install dependencies**

   ```bash
   pip install requests
   ```

3. **Przygotowanie plików / Prepare files**

   - Create `linki-sledzace.txt` with links to analyze.
   - Optionally, prepare `proxy-free.txt` with proxy addresses in the format:

     ```plaintext
     proxy1:port
     proxy2:port
     ```

---

## Użycie / Usage

1. **Przygotowanie pliku wejściowego / Prepare input file**

   Place links in `linki-sledzace.txt` (they can be embedded in text). Example:

   ```plaintext
   1. MetaOSINT: https://lnkd.in/dhX755tY
   2. Bellingcat’s Online Toolkit: https://lnkd.in/e6Q3w5Fk
   3. OSINT Framework: https://lnkd.in/dUyVYSZz
   ```

2. **Uruchomienie skryptu / Run the script**

   ```bash
   python3 resolve_links.py
   ```

3. **Wynik / Results**

   The script creates `wyniki-linki-sledzace.txt` with resolved links:

   ```plaintext
   1. MetaOSINT: https://lnkd.in/dhX755tY -> https://metaosint.github.io/
   2. Bellingcat’s Online Toolkit: https://lnkd.in/e6Q3w5Fk -> https://bellingcat.gitbook.io/toolkit
   3. OSINT Framework: https://lnkd.in/dUyVYSZz -> https://osintframework.com/
   ```

   Lines without resolved links are marked as `Unresolved`.

---

## Zaawansowane funkcje / Advanced Features

- **Obsługa proxy / Proxy Support**  
  If `proxy-free.txt` contains proxy addresses, the script will use them for connection issues.

- **Logi / Logging**  
  All errors and events are logged in `url_resolver.log`, useful for debugging.

- **Losowe User-Agenty / Random User-Agents**  
  The script uses dynamic User-Agents to bypass server blocks against automated traffic.

- **Obsługa przekierowań / Redirect Handling**  
  Automatically follows HTTP redirects and records the final URL.

---

## Contributing

If you wish to contribute, please create a pull request. Ensure your code adheres to the style guidelines and includes tests if necessary.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## Licencja / License

This project is licensed under the **MIT License.**
