'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 아래에 코드를 작성해 주세요.

makes = prices.split(";")
boxes = []
#print(makes)

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
