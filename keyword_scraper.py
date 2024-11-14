import requests
from bs4 import BeautifulSoup
import os

def clean_trminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def key_word_scraping(url,key):
    try: 

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        
        lines = list(soup.stripped_strings)

        show_count=0

    
        for index, line in enumerate(lines, 1):
            if key in line:
                show_count += 1
                print(f"{index}. {line}")
        print(f"the word {key} show {show_count}")
    except:
        print("URL not foud")


    


while True:
        user_url=input("Enter URL (or type 'Q' to quit): ")
        if user_url.lower() == 'q':
            clean_trminal()
            break
        user_word=input("Enter word to search (or type 'Q' to quit): ")
        if user_word.lower() == 'q':
            clean_trminal()
            break
        clean_trminal()
        key_word_scraping(user_url,user_word)
        input("...")
        clean_trminal()

    


