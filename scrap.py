import requests
from bs4 import BeautifulSoup
import json
import os


def get_nb_of_pages(url):
    """This function get the number of pages.

    Args:
        url (String): The url of the first page
    """
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        tds = soup.find('div', class_="pager__page-summary")

        print(tds.find('span', class_='pager__page-summary-item--total').text)
