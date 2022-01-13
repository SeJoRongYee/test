a = 254.195  # 실수
b = "456"    # 문자
#형변환 : 특정 타입(종류)에서 다른 종류의 타입으로 바뀌는 것
print(a, type(a), int(a), type(int(a)))   # 실수 -> 정수
print(b, type(b), int(b), type(int(b)))   # 문자 -> 정수

c = 29    # 정수
d = "True"   # 문자
print(c, type(c), float(c), type(float(c)))
print(d, type(d), bool(d), type(bool(d)))
print(c, type(c), str(c), type(str(c)))

e = "박상용"
# (Castting) 형태 변환
# 문자 형태는 형태 변환 불가