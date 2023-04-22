import sys
PATH = sys.path
PATH.append('C:/Users/gavin/OneDrive/Documents/what_its_worth/env/lib/python3.10/site-packages')
import requests

CLIENT_ID_REDDIT = '8ZrQ3Lr43pcHKbR92XzB-A'
SECRET_KEY_REDDIT = 's9thChLSnIqcibmmWZzhaFF2rY4gRQ'

with open(r'C:\Users\gavin\OneDrive\Documents\what_its_worth\src\pw_reddit.txt', 'r') as file:
    pw_reddit = file.read()

auth_reddit = requests.auth.HTTPBasicAuth(CLIENT_ID_REDDIT, SECRET_KEY_REDDIT)
data_reddit = {
    'grant_type': 'password',
    'username': 'PhobiaStarcraft',
    'password': pw_reddit
}
headers_reddit = {'User-Agent': 'what_its_worth/0.0.1'}
response_reddit_access_token = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth_reddit, data=data_reddit, headers=headers_reddit)

print(response_reddit_access_token.json())

TOKEN_REDDIT = response_reddit_access_token.json()['access_token']
headers_reddit['Authorization'] = f'bearer {TOKEN_REDDIT}'

response_reddit = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers_reddit).json()
print(response_reddit)
