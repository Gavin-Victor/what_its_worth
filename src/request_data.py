import sys
PATH = sys.path
PATH.append('C:/Users/gavin/OneDrive/Documents/what_its_worth/env/lib/python3.10/site-packages')
import requests
from config import headers, base_urls

class RequestData:
    def __init__(self, base_url, end_point_url=None, rest_method=None, headers=None):
        self.base_url = base_url
        self.end_point_url = end_point_url
        self.rest_method = rest_method
        self.headers = headers
        self.url = [base_url, end_point_url]

    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url_components):
        base_url = url_components[0]
        end_point_url = url_components[1]
        if end_point_url:
            self._url = f'{base_url}{end_point_url}'
        else:
            self._url = base_url

    def make_request(self):
        """
        Make a request to the instance url.

        Returns:
            dict: Containing the response from the api.
        """
        response = None
        try:
            response = requests.get(self.url, headers=self.headers).json()
        except Exception as e:
            print(e)
        return response

reddit_base_url = base_urls.get('reddit')
reddit_end_point_url = '/r/TradeAnalyzerFF/'
reddit_end_point_rest_method = 'GET'
reddit_headers = headers.get('reddit')
reddit_request = RequestData(reddit_base_url, reddit_end_point_url, reddit_end_point_rest_method, reddit_headers)
reddit_response = reddit_request.make_request()
print(reddit_response)
