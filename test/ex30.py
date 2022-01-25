# dict(dictionary) : 사전형
# 사전과 같이 "단어 : 뜻" 으로 전개되는 자료형으로 비순서형
# 키를 혀용하지 않으며, 키 : 갑

man = {"name":"박상용", "age":29, "height":176, "weight":79}
print("자료형 종류 : ", type(man), man)

# 열거형 자료 - 순서형 : lsit, tuple
# 열거형 자료 - 비순서형 : set, dict

print("man의 이름 : ", man['name'])        # 특정 항목의 출력
man['name'] = "김성민"                     # 특정 항목의 값 변경
print("man의 이름 : ", man['name'])        # 변경 값 출력
del man['weight']                           # dict에서 해당 항목 삭제
# print(man['weight'])                      # 해당 항목이 삭제됨으로 애러발생
man['kor'] = 90                             # dict에 해당 항목(키 : 값) 추가
print(man)




women = dict(name='김선영', age=25)        # 선언2
print(women['name'], "의 나이: ", women['age'])
