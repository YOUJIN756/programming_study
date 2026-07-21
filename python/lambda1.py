# 1. 람다 함수란?
# 람다 함수는 "이름이 없는 짧은 함수"입니다.
# 일반 함수는 def를 사용하지만,
# 람다 함수는 lambda라는 단어를 사용합니다.
#람다 함수는 짧고 간단한 계산에 적합합니다.

# 일반 함수 형식
# def 함수이름(매개변수):
#     return 계산식
#
# 람다 함수 형식#
# lambda 매개변수: 계산식

print("예제 1. 일반 함수와 람다 함수 비교")
print("=" * 60) #문자 반복

def double(x): # x(매개변수) 받음
    return x * 2

b = lambda x: x * 2
print(b)


#b=double(10) # a(인수) 보냄
print(double(10))

print("거듭제곱 람다 함수")
print("=" * 60) #문자 반복

square = lambda a : a ** 2

print("5의 제곱", square(5))
print("10의 제곱", square(10))

# +, *람다함수(인수를 2개-매개변수 2개)
# 10+20, 4*5
add = lambda a,b : a+b
mul = lambda a,b : a*b

print("10 + 20 =", add(10, 20))
print("4 * 5 =", mul(4, 5))

print("조건식이 들어간 람다 함수")
print("=" * 60)

res = lambda x : "짝수" if x % 2 == 0 else "홀수"

print(res(5))
print(res(10))

print("-" * 50)
print("매개변수가 없는 람다함수")
h = lambda : "안녕하세요"
print(h())

#10와 60중 큰 값을 구하는 람다함수-> 큰 값을 출력
res = lambda x,y : x if x > y else y
print(res(10,60))

print("map()과 람다 함수")
# map()은 리스트의 값을 하나씩 꺼내
# 같은 계산을 반복할 때 사용합니다.
#
# 형식
# map(함수, 리스트)
#
# map()의 결과는 바로 리스트가 아니기 때문에
# list()를 사용하여 리스트로 바꿉니다.

number = [1,2,3,4,5]

result = list(map(lambda x : x * 2, number))
print("원본:", number)
print("결과:", result)

print("map() 으로 점수를 5점 올리기")
score = [78,89,91,56]
score_result = list(map(lambda x : x * 2, score))


print("원본:", score)
print("결과:", score_result)

# filter()는 조건에 맞는 값만 골라냅니다.
#
# 형식
# filter(조건 함수, 리스트)
#
# 람다 함수의 계산 결과가 True이면 남기고,
# False이면 제외합니다.
num=[10,33,45,26,40,88]
lambda x : "3의 배수" if x % 3 == 0 else "아님"
num_list=list(filter(lambda x : x % 3 == 0, num))
# 람다함수 매개변수 x가 리스트에 한개씩 가져오는데
# 람다함수 내 표현식(3의배수)이 맞으면 결과 추출
# 맞지 않으면 버림(제외)=>filter

print(num_list)

#filter()이용하여 합격점수 구하기(70점 이상)
jumsu = [45,60,90,77,55]
jumsu_list=list(filter(lambda j : j>=70, jumsu))
print(jumsu_list)
