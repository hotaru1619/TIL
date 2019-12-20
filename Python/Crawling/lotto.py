import random #내장
import json #내장
import requests #설치 후 사용
# from bs4 import BeautifulSoup as bs # 설치 후 사용

numbers = random.sample(range(1,46),6)
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
print(numbers)

response = requests.get(url)
print(response.text)

lotto = json.loads(response.text)
print(lotto)

#print(lotto["drwtNo6"])
#print(lotto.get("drwtNo6")) # error 방지 위해 선호하는 코드

winner = []

for i in range(1,7):
    winner.append(lotto.get(f"drwtNo{i}"))

print(winner)

# 함수
def pickLotto():
    picked = sorted(random.sample(range(1,46),6))
    matched = len(set(winner)& set(picked))

    if matched == 6 :
        print("1등")
    elif matched ==5 :
        print("3등") 
    elif matched == 4 :
        print("4등")
    elif matched == 3 :
        print("5등")
    else:
        print("꽝")

# import requests
# response = requests.get("https://www.naver.com").text
# print(response)

