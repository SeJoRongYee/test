data = "    you Love mE~? TheJoEun~ Academy  "
print("소문자로 : ", data.lower())
print("대문자로 : ", data.upper())
print("대문자는 소문자로 소문자는 대문자로 : ", data.swapcase())
print("공백 제거전 글자수 : ", len(data))
print("앞의 공백후 제거 글자수 : ", len(data.lstrip()))
print("뒤의 공백 제거후 글자수 : ", len(data.rstrip()))
print("공백 제거후 글자수 : ", len(data.strip()))
print("알파뱃 소문자 o의 개수 : ", data.count("o"))  # 갯수
print("알파벳 대문자 L의 위치 : ", data.find("A"))   # 위치찾기
# find는 만약 찾고자 하는 문자가 없는 경우 -1로 표기
print("알파벳 소문자 o의 위치 : ", data.rfind("o"))  # 오른쪽에서 부터 위치 찾기
print("알파벳 대문자 L의 위치 : ", data.index("L"))   # 위치찾기
# index는 만약 찾고자 하는 문자가 없는 경우 오류가 발생한다.
print("찾아 바꾸기 : ", data.replace("e", "i"))
print("문자열 쪼개기 : ", data.strip().split("~"))
print("특정 문자열로 시작하는지 여부 : ", data.strip().startswith('y'))
print("특정 문자열로 끝나는지 여부 : ", data.strip().endswith('k'))

W = "CaN i HeLp YOu"
print(W.lower())