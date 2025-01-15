# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:51:25 2025

@author: SambesiweSli
"""

from bs4 import BeautifulSoup
import requests

# requesting connection to target website and storing it as a variable
page_to_scrape = requests.get('http://quotes.toscrape.com')

# here we are parsing the html contents of the website.
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# the variables 'quotes' and 'authors' are used to store the information we need
# from the website. Which is the quote and the author.
quotes = soup.find_all('span', attrs={'class':'text'})
authors = soup.find_all('small', attrs={'class':'author'})

# since there are multiple quotes and authors.
# we use the for loop to loop through all of them allowing us to scrape all of
# the quotes along with their authors.
for quote, author in zip (quotes, authors):
    print(quote.text + ' -- ' + author.text + '\n')
    