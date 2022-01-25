data = """나는 자랑스런 대한민국의 국민으로
이름은 박상용이라고 하며,
밀양박씨 이며 , 나이는
29세로 더 조은 컴퓨터 학원에서
python을 배우고 있으며,
잘 이해하고 있다.
"""

lst = []
wd = []
for p in data.split(sep = "\n") :
    lst.append(p)
    for w in p.split(sep = " ") :
        wd.append(w)
print(lst)
print(wd)


# 웹 크롤링하여 필터링 전에 하는 작업


data2 = """Imagine there's no heaven
It's easy if you try
No hell below us
Above us only sky
Imagine all the people
living for today
Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
No religion too
Imagine all the people
living life in peace"""

lst2 = []
wd2 = []
for a in data2.split(sep='\n') :
    lst2.append(a)
    for b in a.split(sep=' ') :
        wd2.append(b)
print(lst2)
print(wd2)


