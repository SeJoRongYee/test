# 알고리즘(algolithm) : 어떤 특정한 문제나 업무를 해결하기 위한 프로그램적 절차나 방범
# 최대값을 계산하는 알고리즘 : 각 값들을 비교하여 가장 큰 값을 찾아내는 절차나 방법.

lst = [90, 75, 95, 80, 85, 70]
max = 0         # 최대값을 저장하기 위해 0으로 변수 초기화
for i in lst :
    if i > max :
        max = i
print(max)

# 최소값 알고리즘

lst2 = [90, 75, 95, 80, 85, 70]
min = lst2[0]
for j in lst2 :
    if j < min :
        min = j
print(min)




