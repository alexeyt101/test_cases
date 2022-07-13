from typing import Dict, List, Optional, Tuple

from bs4 import BeautifulSoup
from requests.exceptions import (ConnectionError, HTTPError, InvalidSchema,
                                 InvalidURL, MissingSchema, Timeout)
import requests

BASE_WIKI_URL = 'https://ru.wikipedia.org'
FIRST_LETTER = 'А' # cyrillic letter
LAST_LETTER = 'Я'


def get_html_page(url: str) -> Optional[str]:
    """Get a html page by url."""
    try:
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Macintosh; '
                                'Intel Mac OS X 10_15_7) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/95.0.4638.69 Safari/537.36'},
                                )
    except (ConnectionError, MissingSchema, InvalidSchema, InvalidURL, HTTPError, Timeout):
        print("Somethins's going wrong during getting the page")
        return None
    return response.text if response.ok else None


def parse_html_page(html_page: Optional[str]) -> Tuple[List[str], Optional[str]]:
    """Parse html page and find all animal names and next page url."""
    if not html_page:
        return [], None

    animal_names_list: List[str] = list()
    soup = BeautifulSoup(html_page, 'lxml')
    mw_pages = soup.find('div', id='mw-pages')

    next_page_url = mw_pages.find_all('a', recursive=False)[-1].get('href')
    next_page_url = BASE_WIKI_URL + next_page_url

    category_columns = mw_pages.find_all('div', class_='mw-category-group')
    for column in category_columns:
        col_letter = column.find('h3').text
        if ord(col_letter) < ord(FIRST_LETTER) or ord(col_letter) > ord(LAST_LETTER):
            next_page_url = None
            break
        col_names = [animal_name.text for animal_name in column.find_all('a')]
        animal_names_list.extend(col_names)

    return animal_names_list, next_page_url


def calculate_count_of_animal_names_for_each_letter(animal_names_list: List[str]) -> Optional[Dict[str, int]]:
    """Get count of animal names for each letter of the alphabet"""
    if not animal_names_list:
        return None

    count_of_names: Dict[str, int] = {chr(i): 0 for i in range(ord(FIRST_LETTER), ord(LAST_LETTER) + 1)}
    count_of_names[chr(1025)] = 0 # cyrillic letter 'Ë'
    for name in animal_names_list:
        first_letter = name[0].upper()
        if first_letter in count_of_names:
            count_of_names[first_letter] += 1

    return count_of_names


def get_count_of_animal_names_for_each_letter(url: str) -> Tuple[List[str], Optional[Dict[str, int]]]:
    """
    Get a list of animals from Wiki and calculate the number of animal names for each letter of 
    the alphabet.
    """
    animal_names_list: List[str] = list()

    while url:
        html_page = get_html_page(url)
        animal_list, url = parse_html_page(html_page)
        animal_names_list.extend(animal_list)
    
    return animal_names_list, calculate_count_of_animal_names_for_each_letter(animal_names_list)
    

if __name__ == '__main__':
    res = get_count_of_animal_names_for_each_letter('https://inlnk.ru/jElywR')
    
    if not res:
        print('Something was going wrong and returned None type')
    for key, value in res[1].items():
        print(f'{key}: {value}')

# P.S.
# Постарался сделать в соответствии с заданием, поэтому по итогам выполнения имеется полный список
# животных. Если бы не требовалось получение полного списка животных, то думаю, алгоритмически
# более правильно было бы добавлять количество животных на каждую букву при обработке каждой 
# html странички. Также стоит отметить, что в списке животных имеется один элемент у которого
# ord(<first_letter>) = 72 (латинская буква 'H'), видимо опечатка на Wiki

