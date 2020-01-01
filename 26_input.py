# chapter05_02
# 파이썬 사용자 입력
# input 사용법
# 기본타입(str) => 기본타입은 무조건 문자열로 받는다.

# 예제1
name = input("Enter your Name : ")
Job = input("Enter your Job : ")
company = input("Enter your Company : ")

print(name,Job,company)
print(type(name), type(Job), type(company))
print()

예제2
number = input("Enter number : ")
name1 = input("Enter name1 : ")

print("type of number", type(number)) #기본 타입이 str이므로 number를 입력해도 문자 str로 인식
print("type of name", type(name1))
print()

# 예제3(계산) 문자로 받기 때문에 int로 형변환
first_number = int(input("Enter first_number : "))
second_number = int(input("Enter second_number : "))

total = first_number + second_number
print("total : ", total)
print("type : ", type(total))
print()

# 예제4 (float 입력)
first_float = float(input("Enter first_float : "))
second_float = float(input("Enter second_float : "))

total = first_float + second_float
print("total : ", total)
print("input type : ", type(total))
print()
#
# 예제5 (print문에서 바로 입력 받는 방법)
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : "))) # 0번째 입력, 1번째 입력
