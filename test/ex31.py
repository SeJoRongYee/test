# dict의 검사와 반복문 활용
dct1 = dict(name='박상용', age=25)
dct2 = dict(name='김상용', age=24)
print(type(dct1), dct1)
print(type(dct2), dct2)
print("dct1에 age 항목이 있는가?", 'age' in dct1)      # 항목(키)의 존재유무
print("dct1에 height 항목이 있는가?", 'height' in dct1)
if('hieght' in dct1) :
    print(dct1['height'])
else :
    dct1['height'] = 176
    print(dct1['height'])

for key in dct1.keys() :            # dct1에 다음 키가 있으면 반복실행  dict.keys()
    print(key, " : ", dct1[key])

for val in dct1.values() :          # dct1에 다음 값이 있으면 반복실행  dict.values()
    print(val)

for i in dct1.items() :             # dct에 해당 항목의 쌍이 있으면 반복실행 dict.item()
    print(i)


for a in [dct1.values() and dct2.values()] :
    print(a)




dct3 = dict(brand='삼성', name='갤럭시', number=22)
dct4 = dict(brand='애플', name='아이폰', number=14)

if 'price' in dct3 and dct4 :
    print(dct3['price'], dct4['price'])
else :
    dct3['price'] = 899
    dct4['price'] = 999
    print(dct3['price'], dct4['price'])
print(dct3, dct4)