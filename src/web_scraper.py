import sys
PATH = sys.path
PATH.append('C:/Users/gavin/OneDrive/Documents/what_its_worth/env/lib/python3.10/site-packages')
from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url, search_list):
        self.url = url
        self.search_list = search_list
        self.web_page = url

    @property
    def web_page(self):
        return self.web_page
    
    @web_page.setter
    def _web_page(url):
        _web_page = requests.get(url)
        return _web_page
    
    def scrape(self, web_page=None, search_list=None):
        """
        Retrieves all of the elements of the passed web page as defined in the passed search_dict.

        Args:
            web_page (request, optional): The web page to be scraped. Defaults to None.
            search_dict (list, optional): A list of dicts containing html tags and class attributes. Defaults to None.

        Returns:
            list: Containing the results from the scrape.
        """
        try:
            result = list()
            parsed_web_page = BeautifulSoup(web_page.text, 'html.parser')
            for search_dict in search_list:
                html_tag = search_dict.get('html_tag')
                class_attribute = search_dict.get('class_attribute')
                scraped_data = parsed_web_page.findAll(html_tag, attrs={'class': class_attribute})
                result.append(scraped_data)
        except Exception as e:
            print(e)
        return result
