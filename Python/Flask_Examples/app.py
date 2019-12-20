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

@app.route("/dday")
def dday():
    today = datetime.datetime.now()
    print(today)
    final = datetime.datetime(2020,6,9)
    result = final - today
    print(result)
    return f"수료까지{result.days}일 남았습니다."


# is it christmas 실습
# "/christmas"
@app.route("/chrestmas")
def isitxmas() :
    today = datetime.datetime.now()
    #print(today.date())
    month = today.date().month
    day = today.date().day
    print(today.date().strftime("%y년 %m월 %d일"))
  
    if month == 12 and day ==25 : 
        return "<h1>yes</h1>"
    else :
        return "<h1>NO</h1>"

#     print(today)
#     final = datetime.datetime(2019,12,25)
#     result = final - today
#     print(result)
# #    return f"{result.days}일 남았습니다."
#     if result.days == 0 :
#         return "yes"
#     else : 
#         return "no"

@app.route("/movies")
def movies() :
    movies = ["겨울왕국2", "클라우스", "어바웃타임", "나홀로집에1","러브액추얼리"]
    return render_template("movie.html", movies = movies, text = "영화 목록")       
                                        # jinja     here

@app.route("/greeting/<name>")
def greeting(name) :
    print(name)
    return f"안녕하세요! {name}님!"

@app.route("/cube/<int:num>")
def cube(num) :
    result = num ** 3
    return str(result)

# 식사 메뉴 추천
# 1. random
# 2. DR_url :  @app.route("/lunch/1 2 3 4")
# - List : ["자장면", "짬뽕", "오므라이스", "볶음밥", "떡볶이", "김밥"]
# - <int:num> 숫자 만큼 뽑기
# 3. print(선택된 메뉴들)

@app.route("/lunch/<int:num>")
def lunch(num) :
    menu = ["자장면", "짬뽕", "오므라이스", "볶음밥", "떡볶이", "김밥"]
    print(random.sample(menu, num))
    # return f"{random.sample(menu, num)}"

    c_menu = random.sample(menu, num)
    return render_template("movie.html", movies=c_menu, text = "점심 메뉴") # 템플릿 공유

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

