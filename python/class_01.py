

class Student:
    s_name="중앙직업전문학교"







s1 = Student("홍길동",90)
s2 = Student("유관순",75)

s2.score=99
s1.print_info()
s2.print_info()

Student.s_name="글로벌 학교"
print("학교명:",Student.s_name)

print("\n"+"="*50)
print("파이썬의 함수 오버로딩")

class Calculator:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c

c1 = Calculator()
print(c1.add(10,20,30))
print(c1.add(100,200))
#파이썬에서는 같은 이름의 함수 여러번 작성하면
#마지막 작성한 함수가 앞의 함수를 덮어씀





