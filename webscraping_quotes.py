# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:51:25 2025

@author: SambesiweSli
"""

from bs4 import BeautifulSoup
import requests

# requesting target website and storing it as a variable
page_to_scrape = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

quotes = soup.find_all('span', attrs={'class':'text'})
authors = soup.find_all('small', attrs={'class':'author'})

for quote, author in zip (quotes, authors):
    print(quote.text + ' -- ' + author.text)
    