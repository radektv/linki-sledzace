import requests
import re
import time
import logging
from random import randint, choice
import urllib3

# Wyłączanie ostrzeżeń SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Konfiguracja loggera
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="url_resolver.log",
    filemode="w"
)

# Funkcja, która wyciąga URL z tekstu
def extract_url(line):
    match = re.search(r'(https?://[^\s]+)', line)
    return match.group(0) if match else None

# Funkcja do ładowania proxy z pliku proxy-free.txt
def load_proxies_from_file(filename="proxy-free.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        logging.error(f"Proxy file {filename} not found.")
        return []

# Lista różnych User-Agentów z przeglądarkami Chrome, Edge i Safari
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Edg/91.0.864.64 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
]

# Funkcja do rozwiązywania URL i zapisania wyników
def resolve_urls(input_file, output_file, max_retries=3):
    headers = {
        'User-Agent': choice(user_agents),
        'Referer': 'https://www.linkedin.com',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }

    proxies = load_proxies_from_file()
    if not proxies:
        logging.warning("No proxies available in the proxy-free.txt file.")

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
            url = extract_url(line)
            if url:
                logging.info(f"Resolving URL: {url}")
                resolved_url = try_resolve_url(url, headers, None)

                if not resolved_url:
                    attempts = 0
                    while attempts < max_retries:
                        proxy = {"http": f"http://{choice(proxies)}", "https": f"http://{choice(proxies)}"} if proxies else None
                        resolved_url = try_resolve_url(url, headers, proxy)
                        if resolved_url:
                            break
                        attempts += 1
                        time.sleep(randint(2, 5))

                if resolved_url:
                    logging.info(f"Resolved URL: {resolved_url}")
                    outfile.write(f"{line.strip()} -> {resolved_url}\n")
                else:
                    logging.warning(f"Could not resolve URL: {url}")
                    outfile.write(f"{line.strip()} -> Nierozwiązane\n")
            else:
                logging.warning(f"No valid URL found in line: {line.strip()}")
                outfile.write(f"{line.strip()} -> Brak URL\n")

            time.sleep(randint(2, 5))

# Funkcja do próby rozwiązania URL z opcjonalnym proxy
def try_resolve_url(url, headers, proxy):
    try:
        response = requests.get(url, headers=headers, proxies=proxy, allow_redirects=True, timeout=10, verify=False)
        if response.status_code == 200:
            return response.url
    except requests.exceptions.RequestException as e:
        logging.error(f"Error resolving URL {url}: {e}")
    return None

# Uruchamianie głównej funkcji
resolve_urls('linki-sledzace.txt', 'wyniki-linki-sledzace.txt')
