# 리스트(순서자료구조)의 추가, 삭제, 수정, 삽입

lst = ["가", "나", "다", "라", "마", "바"]
print(lst)
lst.append("사")
print(lst)

print("삭제 전 : ", lst)
lst.remove("나")
print("삭제 후 : ", lst)

print("변경 전 : ", lst)
lst[0] = "하"
print("변경 후 : ", lst)

print("삽입 전 : ", lst)
lst.insert(2, "파")
print("삽입 후 : ", lst)       # 리스트는 가공을 하면 항상 순서를 유지한다.