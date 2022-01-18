# 제어문 : 조건문, 반복문, 기타 제어문
# 제어문 블록은 해당 명령의 첫 줄에 ":" 이 포함되고, 탭으로 해당 문장들을 블록처리 해야함~
# 조건문 : 주어진 조건에 따라 실행을 달리 하도록 하는 문장  -> if 문장
# 반복문 : 실행 내용을 반복해야할 필요성이 있을 경우 사용하는 문장 -> while, for 문장 등
# 기타 제어문 : continue, break

# 조건문
data = 55
if data >= 80 :      # 단순 if문
    print("합격")
if data <= 80 :
    print("불합격")


if data >= 80 :
    print("합격")
else :
    print("합격이 아님")

if data >= 90 :
    print("수")
elif data >= 80 :
    print("우")
elif data >= 70 :
    print("미")
elif data >= 60 :
    print("양")
elif data >= 0 :
    print("가")

jum1 = int(input("국어 점수를 입력하세요"))
jum2 = int(input("영어 점수를 입력하세요"))
jum3 = int(input("수학 점수를 입력하세요"))
# 복수 조건에서 and 연산자
if jum1 >=70 and jum2 >=70 and jum3 >=70 :
    print("합격")
else :
    print("과락")
# 복수 조건에서  or 연산자
if jum1 >=90 or jum2 >=90 or jum3 >=90 :
    print("과목우수")
else :
    print("해당없음")

# 삼항 조건 if
# 변수 = 참 if (조건식)
# num에는 jum1아 크면 jum1이 입력, jum2가 크면, jum2가 입력됨 -> 최댓값 구할때 사용
num = jum1 if (jum1 > jum2 and jum1 > jum3) elif jum2 (jum2 > jum3) else jum3
print("점수가 더 큰 과목 점수 : ", num)

ScoreA = int(input("Writing Your ScoreA : "))
if ScoreA >= 95 :
    print("A+")
elif ScoreA >= 89 :
    print("A")
elif ScoreA >= 80 :
    print("B")
else :
    print("C")
ScoreB = int(input("Writing Your ScoreB : "))
if ScoreB >= 95 :
    print("A+")
elif ScoreB >= 89 :
    print("A")
elif ScoreB >= 80 :
    print("B")
else :
    print("C")
Total = ((ScoreA + ScoreB)/2)
print(Total)
if Total >= 85 :
    print("pass")
else :
    print("false")