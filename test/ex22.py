# 자료 구조 : 자료가 저장되는 방식 또는 원리
# 스택(last in first out [LIFO]구조), 큐(first in first out [FIFO]구조), 데크(스택+큐)
# 비순서형 : 그래프, 트리
# 열거형 : list, tuple, set, dict

# 순서 자료 구조
# 리스트 선언시 열거형변수명입력 = [요소1, 요소2, ..., 요소n]
lst = ["김", "이", "박", "최", "정", "오"]    # 입력
print(lst)
print(lst[2])
print("lst의 타입 : ", type(lst))

# 문자열은 모두 순차 자료
object = 2022
# print(type(object))           -> int
str_data = str(object)
# print(type(str_data))         -> str
str_data2 = "올해는 "+str_data
print(str_data2)
print(str_data2[4])
print(str_data2[:2])
