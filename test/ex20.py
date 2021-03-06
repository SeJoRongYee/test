# 중첩 반복문
# 2*1=2
# 2*2=4
# ...
# 2*9=18
# 3*1=3
# ...
# 9*9=81

for i in range(2,10) :          # 외부  8번
    for j in range(0,10) :      # 내부  9번
        print(i, "*", j, "=", i*j)

# 중첩 for문은 외부 for문이 한 번 실행에 내부 for문이 0~n번 실행됨
# 2,1~9
# ....
# 9,1~9
# 그러므로 전체 print문이 실행되는 횟수 72번 실행됨


for a in range(2,10) :
    print("---{}단".format(a))
    for b in range(1,10) :
        print("%d * %d = %d"%(a, b, a*b))