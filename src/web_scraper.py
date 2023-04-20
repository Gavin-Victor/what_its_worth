import sys
PATH = sys.path
PATH.append('C:/Users/gavin/OneDrive/Documents/what_its_worth/env/lib/python3.10/site-packages')
from selenium import webdriver

url = 'https://www.ebay.com/sch/i.html?_nkw=INSIGNIA+50-inch+Class+F30+Series+TV&LH_Complete=1&LH_Sold=1&LH_ItemCondition=3000'
browser = webdriver.Chrome()
x_path = '//*[@id="srp-river-results"]/ul/li[4]/div/div[2]/div[4]/div[1]/span/span'
browser.get(url)
price = browser.find_element('xpath', x_path).text
print(price)
