import requests
import random

# Replace this with your raw GitHub URL
QUOTE_FILE_URL = "https://raw.githubusercontent.com/Codingeek4/Music-Department-Quotes/refs/heads/main/music-dmpt_quotes.txt"

def get_random_quote():
    try:
        response = requests.get(QUOTE_FILE_URL)
        response.raise_for_status()
        quotes = response.text.strip().splitlines()
        if not quotes:
            return "No quotes found."
        return random.choice(quotes)
    except requests.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(get_random_quote())
