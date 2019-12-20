from flask import Flask, render_template, request
from decouple import config
import requests
import random

app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

app_url = f"https://api.telegram.org/bot{token}"

# root http://127.0.0.1:5000/
@app.route('/')
def hello() :
    return "안녕하세요!"

@app.route('/write')
def write() :
    #HTML file
    return render_template("write.html")

@app.route('/send')
def send() :
    message = request.args.get("message")
    message_url = app_url + f"/sendMessage?chat_id={chat_id}&text={message}"
    # message 받아서 telegram에게 메시지 보내는 요청
    requests.get(message_url)
    return "메시지 전송 완료했어요!" 

#webhook
@app.route(f"/{token}", methods = ['POST'])    
def telegram():
    print(request.get_json())
    response = request.get_json()

    #실습1 : 사용자의 아이디랑 텍스트 ["update_id"]
    chat_id = response["message"]["chat"]["id"]
    text = response["message"]["text"]
    #print(chat_id)
    #print(text)
    
    #앵무새
    #실습2 : 텔레그램에게 메시지 보내기 요청
   

    # test > 메시지의 내용
    # if 만약 /로또 입력이 되면 text > 6개 숫자를 추천
    if text == "/로또":
        result = []
        [result.append(sorted(random.sample(range(1,46),6))) for _ in range(5)]
        text = result
    
    elif text == "/점심":
        menus = ["20층", "양자강", "맥도날드", "바스버거"]
        text = random.choice(menus)

    message_url = app_url + f"/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(message_url)


    #return body, status_code
    return '', 200


# debug
if __name__ == "__main__" :
    app.run(debug=True)

