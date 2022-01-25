# 양식 문자
rad = 20
pi = 3.141592
l = 2 * rad * pi
a = rad**2 * pi
print("반지름 : ", format(rad, "8d"))
print("원주율 :", format(pi, "5.3f"))
print("원의 둘레 : ", format(l, "2.4f"))
print("원을 면적 :", format(a, "7.1f"))
# 표시형식 코드 = 양식 문자
# f : 실수의 소수점 이하 자릿수 -> .3f 는 소수점 3번째 자리까지 출력
# d(deciomal) : 정수 표시할 자릿수  -> 1000, 8d로 입력 ->     1000 <기존 숫자 자릿수를 빼고 앞에 칸을 빈공간으로 둔다>
# o(octo) : 8진수 정수로 표시 - 89, 3o   -> 111
print("8진수로 출력 : ", format(89, "3o"))
var1 = "박상용"
var2 = 29
var3 = 100.597
lst = (var1, var2, var3)
print("이름 : %s, 나이 : %d, 아이큐 : %3.2f" % (lst))
# x(hexa) : 16진수 정수로 표시 -
print("16진수로 출력 : ", format(157, "5x"))
# s(string) : 문자열을 표시
print("면적 : ",a)


H = int(input("높이 : "))
L = float(input("길이 : "))
A = print("A = ", H*L)