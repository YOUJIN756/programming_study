print("sort()와 람다함수")
# 리스트 안에 튜플
# 순서 있음 : 리스트 [], 튜플()=>불변
# 순서 없음 : 집합 {} => 중복 없음
# 딕셔너리 : {} => 키 : 값

students =[
    ("홍길동", 60),
    ("권율", 92),
    ("이순신", 88),
    ("유관순", 74)
]
#sorted(정렬할 자료,key=정렬기준)
stu_list=sorted(students,key=lambda x : x[1])

#students 리스트를 정렬하되, 각 학생의 두 번째 위치인
# 점수를 기준으로 정렬하라는 뜻
# sorted()는 자료를 정렬하며 기본값은 오름차순(작->큰)
print("오름차순")
print(stu_list)
for a in stu_list:
    #stu_list 요소를 꺼내서 a 변수에 대입
    print(a)
    
stu_list=sorted(students,key=lambda x : x[1])

#reverse : 역순(거꾸로)
print("내림차순")
print(stu_list)
print("=" * 50)
print("딕셔너리->리스트의 정렬")
stu=[
    {"name":"홍길동","score":70}, #item이 2개
    {"name":"아이유","score":88},
    {"name":"변우석","score":95},
    {"name":"유재석","score":52}    
]
# "name" , "score" : 키
# "유재석" , 52 : 값
# 점심 기준으로 내림차순
stu_desc = sorted(stu,key=lambda s : s[1],
                reverse=True)

print("점수가 높은 순서부터 출력")

for ss in stu_desc:
    print(ss["name"],ss["score"])
    
    


