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
        print(self.url)

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
            resp = requests.get(self.url, headers=self.headers)
            print(resp)
            response = resp.json()
        except Exception as e:
            print(f'The following exception occurred: {e}')
        return response
    
    @staticmethod
    def get_reddit_poll_url(response_dict):
        """
        Gets the reddit poll urls from a subreddit response json dictionary.

        Args:
            response_dict (dict): Containing the data from a subreddit.

        Returns:
            list: A list of reddit poll urls.
        """
        try:
            reddit_poll_list = list()
            for post in response_dict['data']['children']:
                post_data = post['data']
                post_selftext = post_data['selftext']
                if '[View Poll]' in post_selftext:
                    poll_url = post_selftext.split('[View Poll]')[1][1:-2]
                    reddit_poll_list.append(poll_url)
        except Exception as e:
            print(e)
        return reddit_poll_list

reddit_base_url = base_urls.get('reddit')
reddit_end_point_url = '/r/TradeAnalyzerFF/'
reddit_end_point_rest_method = 'GET'
reddit_headers = headers.get('reddit')
reddit_request = RequestData(reddit_base_url, reddit_end_point_url, reddit_end_point_rest_method, reddit_headers)
reddit_response = reddit_request.make_request()
reddit_poll_urls = reddit_request.get_reddit_poll_url(reddit_response)
print(reddit_poll_urls)
reddit_poll_response_list = list()
for url in reddit_poll_urls:
    end_point_url = url.split('www.reddit.com')[1]
    reddit_poll_request = RequestData(base_url=reddit_base_url, end_point_url=end_point_url, rest_method=reddit_end_point_rest_method, headers=reddit_headers)
    reddit_poll_response = reddit_poll_request.make_request()
    reddit_poll_response_list.append(reddit_poll_response)

print(reddit_poll_response_list[0])
