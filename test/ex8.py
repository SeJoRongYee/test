# 대입 연산자
a = 100     # a라는 저장소에 100을 저장하라
b = 20
c = b = a
print(a, b, c)
a += 1
print("a : ", a)                             # a가 1이 더해진 값을 다시 a에 대입 101
a += 2
print("a : ", a)
a = a - 1
print("a : ", a)
a -= 1
print("a : ", a)
c = b = a
print(a, b, c)

i = 20
j = 30
print("i =", i,"J =",  j)
#imsi = i                        # 파이썬 이외의 방법
#i = j
#j = imsi
i, j = j, i
print("i =", i,"J =",  j)

lst = (10, 30, 15, 20, 25)
print(lst)
v1, *v2 = lst
print(v1, v2)
*v1, v2 = lst
print(v1, v2)
