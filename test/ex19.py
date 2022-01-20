# 반복문 : while, for가 있다.
# while과 for의 차이
# while : 반목 횟수나 카운트변수가 별도로 지정됨
# for : 반복 횟수나 카운트변수가 내포됨.
# for 변수 in 열거형객체 :
#    실행문
# 열거형 객체 : lst, tuple, set, dict -> 배열


lst = ["박상용", "홍길동", "정몽주", "김두환"]          # 열거형 객체
print(lst)
for i in lst :                  # 분리해서 출력
    print("회원명 : ", i)

# range(begin, end) 함수를 활용
for a in range(1, 20) :
    print(a)

for b in range(7) :         # 하나의 숫자만 적힌경우는 end값으로 인식
    print(b)

for c in range(1, 20, 3) :          # 새 번째 인수는 step
    print(c)

import random
lst2 = []
for d in range(10) :       # 0~9
    r = random.randint(2, 20)
    lst2.append(r)          # append : 요소 추가
    print(r)
print("lst2 : ", lst2)