# random 모듈을 활용하여 주사위를 두 개 던졌을 때 두 개의 주사위 결과를 출력
import random
a = random.randint(1, 6)
b = random.randint(1, 6)
print(a, b)

c = 0
while c < 6 :
    c+=1
    print(random.randint(1, 45))

while True :
    a = int(input("숫자를 입력하세요"))
    b = random.randint(1, 10)
    if a == b :
        print("성공", a)
        break
