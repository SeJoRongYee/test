# 논리 연산자 : 여러 비교연산자를 이어 붙여 조건을 판단할 떄 사용
var1 = 60
var2 = 50
var3 = 40
var4 = 70
print("var1 >= var2 and var3 >= var4", var1 >= var2 and var3 >= var4)
# 'and' 논리는 모든 조건이 만족해야 True 그렇지 않은 경우는 False

print("var1 >= var2 or var3 >= var4 or var1 <= var4", var1 >= var2 or var3 >= var4 or var1 <= var4)
# 'or' 논리는 주어진 조건중 하나만 만족해도 True 모두 거짓이어야 False

print("not (va1 >= var2) : ", not (var1>=var2))
# 'not' 논리는 모든 결과를 반대로 출력해준다.
