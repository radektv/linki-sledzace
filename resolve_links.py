import requests
import re

# Funkcja, która wyciąga URL z tekstu
def extract_url(line):
    # Używamy wyrażenia regularnego, aby znaleźć URL
    match = re.search(r'(https?://[^\s]+)', line)
    if match:
        return match.group(0)
    return None

# Funkcja do rozwiązywania URL i zapisania wyników
def resolve_urls(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
            url = extract_url(line)
            if url:
                try:
                    # Wykonujemy zapytanie do URL
                    response = requests.get(url, allow_redirects=True)
                    # Jeśli uda się pobrać stronę, zapisujemy wynik
                    resolved_url = response.url
                    outfile.write(f"{line.strip()} -> {resolved_url}\n")
                except requests.exceptions.RequestException as e:
                    # Jeśli wystąpi błąd, zapisujemy informację o błędzie
                    outfile.write(f"{line.strip()} -> Error: {str(e)}\n")
            else:
                # Jeśli URL nie zostanie znaleziony, zapisujemy oryginalną linię
                outfile.write(f"{line.strip()} -> Error: No valid URL found\n")

# Użycie funkcji do rozwiązywania URL
resolve_urls('linki-sledzace.txt', 'wyniki-linki-sledzace.txt')
