import sys
PATH = sys.path
PATH.append('C:/Users/gavin/OneDrive/Documents/what_its_worth/env/lib/python3.10/site-packages')
from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url):
        self.url = url
        self.web_page = url

    @property
    def web_page(self):
        return self._web_page
    
    @web_page.setter
    def web_page(self, url):
        self._web_page = requests.get(url)
    
    def scrape(self, search_list):
        """
        Retrieves all of the elements of the passed web page as defined in the passed search_list.

        Args:
            search_list (list, optional): A list of dicts containing html tags and class attributes.

        Returns:
            list: Containing the results from the scrape.
        """
        try:
            result = list()
            parsed_web_page = BeautifulSoup(self.web_page.text, 'html.parser')
            for search_dict in search_list:
                html_tag = search_dict.get('html_tag')
                class_attribute = search_dict.get('class_attribute')
                scraped_data = parsed_web_page.findAll(html_tag, attrs={'class': class_attribute})
                for element in scraped_data:
                    result.append(element.text)
        except Exception as e:
            print('Exception occurred')
            print(e)
        return result
