# 변수명은 알파벳으로 시작하고, 대소문자를 구분하며, 예약어를 사용할 수 없다
# print <-예약어(Reserved word) : print<x> print1<0>
# 중간에 띄워쓰기하면 안됨
# printNumber<o> : 카멜 방식, 단어를 읽기 쉽도록 두 번쨰 단어부터
# 첫 글자를 대문자로 표기하는 방식 -> printNumberCaption
# print_number<o> : 언더스코어 방식, 단어마다 중간 언더스코어<_>를 넣는다.
# print_number_caption


# 예약어 출력
import keyword
print(keyword.kwlist)

# 식별자(Identifiers) : 변수, 클래스, 모듈, 함수