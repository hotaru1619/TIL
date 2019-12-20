

# Python 101

## 1. 저장

### 1) 숫자
### 2) 글자

String 조작하기

1. 글자 합체

   ```python
   hphk = "happy" +" " + "hacking"
   
   print(hphk)
   
   => happy hacking
   ```

2. 글자 삽입 : .format() , f{변수}

   ```python
   name = "tony"
   age = 20
   
   text = "제 이름은 {}입니다. 나이는 {}살 입니다!".format(name, age)
   
   print(text)
   
   f_text = f"제 이름은 {name}입니다. 나이는 {age}살 입니다!"
   print(f_text)
   ```

3.  글자 자르기 : split

   ```python
   # string > "어떠한 글자들"[start : end]
   text_name = text[:15]
   print(text_name)
   text_age = text[15:]
   print(text_age)
   
   text_split = text.split()
   print(text_split)
   
   ```

### 3) 참/거짓

```python
# input 표준입력
a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

if a>=90 and b>80 and c>85 and d>=80 :
    print(True)
else : 
    print(False)
```



## 2. 조건

```python
number = int(input('숫자를 입력하세요: '))
print(number % 2)

if number %2 ==1 :
    print("홀수입니다.")
else : 
    print("짝수입니다.")

# 1 > True
# 0 > False
if number %2  :
    print("홀수입니다.")
else : 
    print("짝수입니다.")
```



## 3. 반복 : for

range()

```python
menus =  ["순남 시래기", "양자강", "20층", "바스버거"]

for menu in menus:
    print(menu)

# print (range(4)) 
print("==========")
for i in range(4):
    # print(i)
    print(menus[i])    
```



```python
n = int(input('숫자를 입력하세요: '))

for i in range(n):
    print(i+1)

print("--------------")
for i in range(1, n+1):
    print(i)

```



## 4. 기타

```python
# List
menus = ["순남 시래기", "양자강", "20층"]
print(menus)
print(menus[0])

# Dictionary(key : value)
dict_nums = {"순남 시래기" : "02-1234-2345", "양자강" : "02-9876-6543", "20층" : "02-1111-7777"}
print(dict_nums["순남 시래기"])
print(dict_nums.get("시래기")) # None

```

```python
sample = input("문자를 입력해주세요! : ")
print(sample[0])
print(sample[-1]) 
# -1 : 맨 뒤 인덱스

print(f"첫 글자 : {sample[0]}")
print(f"마지막 글자 : {sample[-1]}")
```

check!!!! boxes.sort(reverse=True)

```python
prices = input('물품 가격을 입력하세요: ')

makes = prices.split(";")
boxes = []
#print(makes)
#1000;3000;5000;1
#['1000', '3000', '5000', '1']
# list > append : list에 data를 넣어줌.
for make in makes:
    # print(type(make))
    print(make)
boxes.append(int(make))
#print(sorted(boxes)) # 순서 바뀌지 않음.
#print(boxes)

# list > sort()
boxes.sort(reverse=True) # 큰 숫자부터 출력
print(boxes)
#print(len(boxes))
#print(len("123453"))

```

## 5. WEB Crawling

### 1) lotto.py

```python
import random 
import json
import requests

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
```



### 2) exchange.py

```python
import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/marketindex/"

response = requests.get(url).text
soup = bs(response, 'html.parser')
# . > class
# # > id

exchange = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
change = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.change")
updown = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.blind")
print(f"현재 원.달러 환율은 {exchange.text} 입니다.")
print(f"전일 대비 {change.text}원 {updown.text}하였습니다.")

#파일 저장
with open('test.text', 'w', encoding='utf-8') as f:
    f.write(f"현재 원.달러 환율은 {exchange.text} 입니다.")

    f.write(f"전일 대비 {change.text}원 {updown}하였습니다.")
```

## 6. Flask

```python
from flask import Flask, render_template, request
import datetime
import random
import requests

# 지금부터 flask의 이름이 app
app = Flask(__name__)

# url을 관리해주는 친구 > @app.route("/")
@app.route("/")
def hello():
    return "안녕"

@app.route("/chrestmas")
def isitxmas() :
    today = datetime.datetime.now()
    print(today.date().strftime("%y년 %m월 %d일"))
if month == 12 and day ==25 : 
        return "<h1>yes</h1>"
    else :
        return "<h1>NO</h1>"

    
@app.route("/vonvon")
def vonvon() :
    return render_template("vonvon.html")

@app.route("/godmademe")
def godmademe() :
    name = request.args.get("name")
    print(name)
    
    first_list =["못생김","어중간함", "착하게 생김", "공부 잘하게 생김"]
    second_list = ["애교", "잘난 척", "쑥스러움", "자신감"]
    third_list = ["허세", "식욕", "찌질", "부"]

    f_list = random.choice(first_list)
    s_list = random.choice(second_list)
    t_list = random.choice(third_list)

    return render_template("godmademe.html", name=name, f_list=f_list, s_list=s_list, t_list=t_list)


# flask run
# Debug Mode => python app.py
if __name__ == "__main__":
    app.run(debug = True)
    
```

**return render_template("godmademe.html",** 

**name=name, f_list=f_list, s_list=s_list, t_list=t_list) **

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>vonvon</title>
</head>
<body>
    <h1>신이 당신을 만들 때</h1>
    <form action="/godmademe">
        <input type="text" name="name">
        <input type="submit">
    </form>
</body>
</html>
```



```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>신이{{ name }}를 만들 때</h1>
    <p>{{ f_list }}을 한 스푼...</p>
    <p>{{ s_list }}도 넣어주고...</p>
    <p>그리고 {{ t_list }}를 조그...으어....</p>
</body>
</html>
```

**!! jinja **

**{% for %}**					{% for movie in movies %}	

**{{  }}**								{{ movie }}

**{ %endfor%}**				{%endfor%}