# 반복문 while
i = tot = 0         # 두 변수, i, tot를 모두 0으로 초기화
# while문은 조건이 만족하는 동안 반복 실행하게 됨
# while 조건 :
#   반복실행문장
while i < 10 :
    i+=1            # i가 1식 증가
    tot+=i          # tot에 i를 누적 시킴
print("1부터 10까지의 합계 : ", tot)

i = tot = 0
while i < 100 :
    i+=2
    tot+=i
    print(i)
print("1부터 100까지의 짝수 합계 : ", tot)

dlist = []          # 빈 list
i = tot = 0
while i < 100 :
    i+=3
    dlist.append(i)
print("요소의 값들 : ", dlist)
print("요소의 수 : ", len(dlist))

klist = []
i = tot = 0
while i < 100 :
    i+=1
    if i % 5 == 0 :
        klist.append(i)
print(klist)

tlist = []
i = tot = 0
while True :
    i+=1
    if i > 100 :
        break
    if i % 5 == 0 :
        tlist.append(i)
print(tlist)