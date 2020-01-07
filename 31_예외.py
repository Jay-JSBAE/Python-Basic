# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError(문법 틀렸을때), TypeError, NameError(없는 변수를 참조할때), IndexError, valueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법오류
# print('error)
# print('error'))
# if True    #: 안씀
#    Pass

# Name Error : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) 4번째 뺼게 없으니깐 에러

# KeyError
# dic = {'name': 'jay', 'Age' : 35, 'address' : 'seoul'}
# print(dic['name'])
# print(dic['hobby'])
# print(dic.get('hobby')) #그래서 get으로 가져오는것이 안전, 없으면 None 출력

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time())
# print(time.time2())

# ValueError
# x = [10, 50, 90]
# x.remove(200)
# print(x)

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'
# print(x + y)
# print(x + z)
# print(y + z)
# print(x + list(y)) #형변환 해서 더해줘야함

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

# name = ['Bae', 'Choi', 'Park']

# 예제1
# try:
#     z = 'Cho' # Cho로 했을떈 예외 실행
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z,x+1))
# except ValueError:
#     print('Not Found - ValueError!!!')
# else:
#     print('OK')

# print()

# 예제2 - 모든 에러는 다 잡으나 어떤 에러인지 모르는 단점이 있음
# try:
#     z = 'Kim'  # Cho로 했을떈 예외 실행
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception: # 모든 에러 처리
#     print('Not Found it! - Occurred Error!!!')
# else:
#     print('OK')

# print()

# 예제3 - 예제2를 세련되게
# try:
#     z = 'cho'  # Cho로 했을떈 예외 실행
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception as e:
#     print(e)  # 에러내용 확인
#     print('Not Found it! - Occurred Error!!!')
# else:
#     print('OK else')
# finally:
#     print('OK Finally')

# print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
# 관리자 같은 페이지

try:
    a = 'Park'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occurred! Exception!')
else:
    print('OK else')
