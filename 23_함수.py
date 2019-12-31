# chapter05_01
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lanbda)
# 함수의 장점 - 코드의 복잡도를 단순 / 코드의 재사용성 / 코드의 안정
# 함수 정의 방법
# def function_name(parameter):
#     code

# 예제1
def first_func(w):
    print("Hello ", w)

word = "Python"

first_func(word)
print()

# 예제2
def return_func(w1):
    value = "Hello " + str(w1) # w1에 숫자가 올수있으니 str로 문자 형변환
    return value

x = return_func('python')
print(x)
print()

# 예제3(다중반환)
def func_1(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3 #동시에 다중 리턴
#3개를 리턴하기 때문에 3개를 받아야함
x, y, z = func_1(10)
print(x, y, z)
print()

# 튜플리턴
def func_2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) # 튜플로 패킹되어 노출

q = func_2(20)
print(type(q), q)
print()

# 리스트 리턴
def func_3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

q = func_3(30)
print(type(q), q)
print()

# 딕셔너리 리턴
def func_4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1, 'v2':y2, 'v3':y3}

d = func_4(30)
print(type(d), d)
print(d.get('v1'), d.items(), d.keys(), d.values())
print()

# 중요
# *args,**kwargs

# *args(언팩킹)
def args_func(*args): # 매개변수명은 자유 *a *step 자유 / 매개변수가 가변이라는 거다.
    for i, v in enumerate(args): # 설명 : https://wikidocs.net/32
        print('Result : {}'.format(i), v)
    print('----------------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Jay', 'Park', 'Choi')
print()

def args_func1(nation, *args):
    if nation == "Korea":
        result = 0
        for i in args:
            result = result + i
    elif nation == "Canada":
        result = 1
        for i in args:
            result = result + i
    return result
result = args_func1('Korea', 1,2,3,4,5)
print(result)

# **kwargs(딕셔너리 자료형 언팩킹)
def kwargs_func(**kwargs): #매개변수명은 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v]) # 딕셔너리는 접근할때 get 또는 속성으로 접근
#     print('-----------------')
#
# kwargs_func(name1 = 'Lee')
# kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Kim')
print()

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Jay', 'Park', 'Choi', age1 = 20, age2 = 30, age3 = 40 )
print()

# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
print()

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

#def mul_func(x,y):
#    return x * y

#lambda x, y: x*y 함수의 이름이 없음!
# a = (x,y)
# 일반적 함수
def mul_func(x,y):
    return x * y
q = mul_func(10,50)
print(q)

# 람다 함수
lanbda_mul_func = lambda x,y : x * y
print(lanbda_mul_func(10,50))
print()

# 함수 안에서 함수를 받을때
def func_final(x,y,func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x,y:x*y)
