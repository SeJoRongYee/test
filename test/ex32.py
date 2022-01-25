# 객체나 자료형의 복제
kims = ["김우중","김성민","김기태","김서은"]
lees = ["이강성", "이동은", "이영국", "이몽룡"]
names = kims        # 데이터가 있는 곳의 주소를 전달 -> 얕은 복제
print("kims의 메모리 주소 : ", id(kims), "데이터 : ", kims)
print("names의 메모리 주소 : ", id(names), "데이터 : ", names)
names[3] = "김상용"        # 같은 메모리 주소를 사용하게 됨으로 사본을 바꾸면, 원본도 변경됨
print(kims)
print(names)

import copy                         # 원본을 유지하고 사본만 변경 하는 방법
lst = copy.deepcopy(kims)           # 데이터는 같으니 서로 다른 메모리 주소를 사용 -> 깊은 복제
print(kims, "의 주소 : ", id(kims))
print(lst, "의 주소 : ", id(lst))
lst[3] = "김기태"
print(lst)
print(kims)