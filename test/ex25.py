# 리스트에 요소를 반복문을 활용하여 대입할 수 있다. -> 내포

a = [2, 4, 5, 3, 1]
b = a*2         # 요소의 2배 확장
print(b)
c = [i**2 for i  in a]      # 값이 2제곱이 된다
print(c)

m = []
for k in a :
    m.append(k*2)
print(m)

even = [i for i in range(0,11) if i % 2 == 0]
print(even)