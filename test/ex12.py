# 문자열 저장 및 출력
singleLine = "오늘은 불금인데 뭐하나"
multiLIne = """오늘 저랑
불금을 함께 하실 분을
모십니다
술 한잔 해요"""""
print(singleLine)
print(multiLIne)

data = "i love thejoeun academy"
print(data[0])
print(data[7])
print(data[2:5])            # begin:end  - begin부터 end전 까지
print(data[:6])             # begin 생략시는 처음부터
print(data[7:])             # end생략시 begin부터 끝가지
print(data[1:6:9])          # begin:end:step
print(data[-3])             # 뒤에서 n번째 글자
print(data[-3:])            # 뒤에서 n번째 글자부터 끝까지
print(data[:-3])            # 뒤에서 n번째 글자까지
print(data[-6:-1])
print(data[::2])
print((data[0]*10))         # 처음 글자를 여러번 출력