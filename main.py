#This is the python script for webscraping the Vanderbilt Television News Archive (VTNA)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello")


from bs4 import BeautifulSoup

from selenium import webdriver

import lxml

import xpathwebscrapper
import pandas as pd
import requests
import urllib


url = "https://tvnews.vanderbilt.edu/search?utf8=%E2%9C%93&query=sandyhook+shooting&button"
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="results-list-container"]/ul/li[1]/div/h4/a')

source = requests.get('https://tvnews.vanderbilt.edu/search?utf8=%E2%9C%93&query=sandyhook+shooting&button')

soup = BeautifulSoup("url", 'lxml' )


shootings = soup.find_all('div', class_='search-result')

print(shootings)

for shooting in shootings:
    print(shootings_cards.h4.text)

#print (shootings_cards.a)



