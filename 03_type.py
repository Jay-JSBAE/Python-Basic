# 2019.11.07
'''
변수와 상수

변수
1. 변수는 대소문자를 구분한다.
2. 변수명은 _(언더스코어)나 영문자로 시작한다.
3. 예약어(if, while, for, etc) 변수명으로 사용할 수 없다.
'''

x = 10
y = 20
print(x+y)

name = input('이름을 입력하세요 : ')
age = input('나이를 입력하세요 : ')
print(name, age)
print('제이름은', name, '입니다.', '제 나이는', age ,'입니다.')

#문자열 포맷팅 형식
print('제 이름은 {}입니다. 제 나이는 {}입니다.'.format(name, age))

# 변수의 타입
a = 10
b = 10.1
c = 'jay'
d = True #bool(True, False)
e = [100, 200, 300]
f = (100, 200, 300)
g = {'one':1, 'two':2}
h = {100, 200, 300, 400}

print(type(a),type(b),type(c),type(d))
print(type(e),type(f),type(g),type(h))
