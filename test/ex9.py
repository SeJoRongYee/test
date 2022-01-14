# 표준연산자
va1 = 100
var2 = "박상용"
print(var2, "의 점수는 ", var1, "점 입니다.")       # 표준출력 print
p1 = int(input("국어 점수 입력 : "))               # 표준입력 input
p2 = int(input("영어 점수 입력 : "))
p3 = int(input("수학 점수 입력 : "))
tot = p1 + p2 + p3          # 총점
print("총점 : ", tot)
print("평균 : ", tot/3)