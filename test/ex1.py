print('hello python')  # hello python 을 출력
# 프로그램상에서 필요한 데이터를 저장하거나 연산하려면 저장소가 필요
# 저장소 -> '변수'라고 칭한다. 변수명은 개발자가 정하는 것으로 영문으로 시작해야하며
var1 = "박상용"
var2 = 1004    # 파이썬은 저장하는 데이터에 따라 변수유형이 달라짐
print(var1,var2)   # 올해는 2022 출력

# 영문 대소문자를 구분하며, 두 번째 글자부터는 숫자를 사용할 수 있음
var3 = 3.3141592  #실수(소수점이하가 있는 수) -> 실수형변수
var4 = True  #논리형 변수 : True 아니면 False
print(id(var1), id(var2), id(var3), id(var4))
# 변수의 종류 : 문자열 변수, 정수형 변수, 실수형 변수, 논리형 변수