# 외부 상수의 format 함수 활용
name ="박상용"
age = 29
iq = 100
print("이름 : {}, 나이 : {}. 아이큐 : {}".format(name,age,iq))
print("아이큐 : {2}, 이름 : {0}, 나이 : {1}".format(name, age,iq))

name = str(input("이름을 입력하세요 : "))
age = int(input("나이를 입력하세요 : "))
iq = float(input("아이큐를 입력하세요 : "))
print("이름 : {}, 나이 : {}. 아이큐 : {}".format(name,age,iq))