import requests
from bs4 import BeautifulSoup
from enum import Enum
import os

def clean_trminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_temperature(city_url):

    url = city_url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    temperature = soup.find_all('span', class_='header-temp')  

    for i in temperature:
        text = i.text.strip() 

    return text

def manue():
    print("\nSelect a city:")
    for direction in Direction:
        print(f"{direction.value}. {direction.name}")




class Direction(Enum):
    TLV = 1
    Jerusalem = 2
    Ashqelon = 3
    Eilat = 4
    Hermon = 5
    Exit = 6


while True:
    manue()
    user=int(input("Enter your choice: "))
    if user == 1:
        clean_trminal()
        print(f"The temperature tel-aviv: {get_temperature("https://www.accuweather.com/en/il/tel-aviv/215854/weather-forecast/215854")}")
        input("...")
    if user == 2:
        clean_trminal()
        print(f"The temperature Jerusalem: {get_temperature("https://www.accuweather.com/en/il/jerusalem/213225/weather-forecast/213225")}")
        input("...")
    if user == 3:
        clean_trminal()
        print(f"The temperature Ashqelon: {get_temperature("https://www.accuweather.com/en/il/ashqelon/215614/weather-forecast/215614?city=ashkelon")}")
        input("...")
    if user == 4:
        clean_trminal()
        print(f"The temperature Eilat: {get_temperature("https://www.accuweather.com/en/il/elat/1-215615_1_al/weather-forecast/1-215615_1_al")}")
        input("...")
    if user == 5:
        clean_trminal()
        print(f"The temperature Hermon: {get_temperature("https://www.accuweather.com/en/us/hermon/61458/weather-forecast/2241154?city=hermon")}")
        input("...")
    if user == 6:
        clean_trminal()
        print("Goodbey!")
        exit()



