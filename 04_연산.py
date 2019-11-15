"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x의 y제곱 = x**y
"""

# 산술연산
x = 20
y = 10
z = -40
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 실수형
print(x ** 2) # x의 제곱
print(x % 3) # 나머지 출력
print(abs(z))
print()

# 비교연산
a = 10
b = 20
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)
print()

# 할당연산
c = 10
c += 30 # c = c + 30
c -= 20
c //= 20
c *= 10
print(c)
print()

# 논리연산
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print()

# bit 연산
d = 13
e = 11
print(d & e)
print(d | e)
'''
가까운 2의 배수로 계산
   1101
 & 1011
   1001 => 9
'''
