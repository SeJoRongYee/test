# set의 사용법 : 중복성을 해결할 때
# 도메인 : 하나의 데이터 그룹에서 중복되지 않은 항목이 가져야 할 값들
domain = ["서울", "대전", "대구", "부산", "서울", "광주", "대전", "부산"]
print(domain)
city = set(domain)      # 중복성을 해결하려면 특정 자료형에서 set로 변환
print(city)

data = """박상용 심인보 이동주 박상용
정몽주 이순신 광대토대왕 심인보 이동주 정몽주 이순신
박상용 심인보 이재명 윤석열 박상용 이재명
윤석열 심인보 이재명 박상용 이순신 정몽주"""

lst1 = data.split(sep='\n')
lst2 = []
for i in range(0, len(lst1)) :
    lst2.append(lst1[i].split(sep=" "))
print(lst2)
st1 = set(lst2)