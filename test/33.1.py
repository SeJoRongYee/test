import random

lst1 = []
for i in range(6) :
    r = random.randint(1,20)
    lst1.append(r)
    print(r)
lst1.sort()
print(lst1)

max = lst1[0]
for a in lst1 :
    if a > max :
        max = a
print(max)