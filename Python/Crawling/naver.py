'''
1. requests > naver.com
2. response > bs4
3. webbrowser
'''
import requests
from bs4 import BeautifulSoup as bs

import webbrowser

url = "https://www.naver.com"
response = requests.get(url).text

#print(response)

# 'html.parser' > 받아올 형식
doc = bs(response, 'html.parser')
# . > class
# # > id 
result = doc.select('.ah_k')
#result = doc.select_one('.ah_k') 
#result = doc.select_one('#themcast') 
print(result)

#webbrowser.open(url)
search_url = "https://search.naver.com/search.naver?query="
for i in range(5):
    webbrowser.open(search_url + result[i].text)

    #print(result[i].text)
