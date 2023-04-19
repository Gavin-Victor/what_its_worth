import sys
PATH = sys.path
PATH.append('C:/Users/gavin/OneDrive/Documents/what_its_worth/env/lib/python3.10/site-packages')
from selenium import webdriver

url = 'https://www.youtube.com/watch?v=CHUxmVVH2AQ&t=164s&ab_channel=Hallden'
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('//*[@id="description-inline-expander"]/yt-attributed-string/span').click()
