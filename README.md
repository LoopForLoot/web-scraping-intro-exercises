# Introduction to Web Scraping: Exercises

 As an introduction to learning web scraping, here are two exercises designed to practice fundamental scraping skills. Both exercises use Python's requests library to fetch web page content, along with BeautifulSoup from the bs4 library to parse HTML.

## Exercises

### 1. Get Temperature of 5 Cities
Create a tool that retrieves the current temperature for five specified cities from a weather website. This exercise involves sending a request to the weather site and parsing the response to extract temperature data.

### 2. Find Keyword in a URL
Develop a tool that accepts a URL and a keyword, then searches the web page for occurrences of the keyword. It will display each line where the keyword appears and count the total occurrences. This exercise helps practice working with text data scraped from HTML content.

### Tools and Libraries Used
requests: Sends HTTP requests to retrieve page content.

BeautifulSoup (from bs4): Parses HTML to easily find and extract elements.

### These exercises are meant to provide a hands-on introduction to basic web scraping using Python.


### How to Run:
#### 1. Clone the repository.
   ```bash
    git clone https://github.com/LoopForLoot/python-rock-paper-scissors-game.git
```


#### 2. Install Requirements.
   ```bash
   pip install -r requirements.txt
```

#### 3. Run the Scripts.
   ```bash
   python temperature_scraper.py

   or

   python keyword_scraper.py
```

