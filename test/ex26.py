# tuple
# 열거형으로 순서형 자료구조
# 읽기 전용으로 처음 선언시 초기값 부여만 가능
# 요소의 추가, 삽입, 삭제, 변경이 불가능함
tp = (40, 20, 30, 15, 35, 25)
print(tp)
# tp.append(65)  tuple은 요소의 추가, 삽입, 삭제가 불가
tp2 = tp
print(tp2[2])
lst = list(tp2)         # 요소의 변경, 제거, 삽입, 추가가 필요할 경우
                        # tuple - list - 요소작업 - tuple
print(lst)
lst.append(45)
print(lst)
tp3 = tuple(lst)
print(tp3)

if 40 in tp3 :
    print("40이 존재함")
else :
    print("40이 없음")