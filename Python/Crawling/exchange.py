import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/marketindex/"

response = requests.get(url).text
soup = bs(response, 'html.parser')
# . > class
# # > id

#exchange = soup.select_one(".value")
exchange = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
change = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.change")
updown = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.blind")
print(f"현재 원.달러 환율은 {exchange.text} 입니다.")
print(f"전일 대비 {change.text}원 {updown.text}하였습니다.")

#파일 저장
with open('test.text', 'w', encoding='utf-8') as f:
    f.write(f"현재 원.달러 환율은 {exchange.text} 입니다.")

    f.write(f"전일 대비 {change.text}원 {updown}하였습니다.")