# 리스트끼리 연산(결합, 확장, 추가, 두 배 확장)

# 리스트의 결합
lst1 = ["가", "다", "마", "사"]
lst2 = ["나", "라", "바", "아"]
lst3 = lst1 + lst2
print("결합 후 : ", lst3)

# 리스트의 확장
print("확장 전 : ", lst1)
lst1.extend(lst2)
print("확장 후 : ", lst1)

# 리스트의 추가
lst4 = ["가", "다", "마", "사"]
lst5 = ["나", "라", "바", "아"]
print("추가 전 : ", lst4)
lst4.append(lst5)
print("추가 후 : ", lst4)      # 리스트의 요소가 아닌 리스트자체가 요소로 추가 됨


# 리스트의 두 배 확장
res = lst5 * 2
print("lst5의 두 배 확장 : ", res)

print("정렬 전 : ", lst1)
lst1.sort()
print("정렬 후 : ", lst1)
lst1.sort(reverse = True)
print("역순정렬 후 : ", lst1)


import random
lst6 = []
for i in range(1,10) :
    lst6.append(random.randint(1,9))
print(lst6)

# 리스트의 검사 : 해당 값이 리스트의 존재 여부를 판단
if 6 in lst6 :
    print("6이 존재함")
else :
    print("6이 존재하지 않음")

for m in 6 :
