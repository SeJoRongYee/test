# 비순서형 자료구조 set
# set의 특징 : 중복을 허용하지 않음, 순서 유지가 되지 않음, {}사용

st1 = {80, 85, 75, 70, 80, 85}
print(type(st1), st1, len(st1))     # 순서 유지가 안된다. 따라서 index 존재 하지 않음

st2 = {65, 70, 75, 80}
# st3 = {}        # 공집합은 연산 불가
st3 = st2.union(st1)    # 합집함
st4 = st2.intersection(st1)   # 교집합 메소드(intersection)
st5 = st1.difference(st2)     # 차집합 메소드(difference)
st6 = st2.difference(st1)
print("합집합 : ", st3)
print("교집합 : ", st4)
print("st1 - st2 : ", st5)
print("st2 - st1 : ", st6)

# 관련 메소드 : 원소 추가(add), 원소 삭제(discard)
st1.add(50)
print("st1에 50 원소 추가: ", st1)
st1.discard(70)
print("st1에 70 원소 삭제 : ", st1)