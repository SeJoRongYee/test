# random 수 출력하기 위한 random 모듈을 임포트 시킴
# 임포트란 ? : 파이썬의 내장모듈이 아닌 외장모듈을 불러오기
import random
# help(random)        # 해당 모듈의 속성과 메소드를 보기
a = random.random()     # 0~1 숫자를 임의로 발생
b = random.randint(1, 10)   # 1~10 숫자 중에서 임의로 발생
print(a, b)

blist = ["김기태", "김서은", "김성민", "김우중", "박상용","심인보", "이동은", "성윤식", "이강석", "김민지"]
plist = [0, 1000, 2000, 10000, 0, 0, 100000, 0, 50000, 0]
if '김상민' in blist :
    print("김상민 있음")
else :
    print("김상민 없음")

c = random.randint(0, 4)
print("우수 직원 : ", blist[c])

i = 0
while i < len(blist) :
    i+=1
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    print(blist[c], " : ", plist[d])