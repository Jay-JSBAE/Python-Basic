# 관계 연산자
# >,>=,<,<=,==,!=
x = 15
y = 10

print(x == y) # 양변이 같을때 참
print(x != y) # 양변이 다를때 참
print(x > y) # 왼쪽이 클때 참
print(x >= y)
print(x < y)
print(x <= y)
print()

점수 = 82
if 점수 >= 90:
    print('A+')
if 점수 < 90 and 점수 >= 80:
    print('A')
if 점수 < 80 and 점수 >= 70:
    print('B+')
if 점수 < 70 and 점수 >= 60:
    print('B')

점수1 = 82
if 점수1 >= 90:
    print('A+')
elif 점수1 >= 80:
    print('A')
elif 점수1 >= 70:
    print('B+')
elif 점수1 >= 60:
    print('B')
else:
    print('C')


# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a>b and b>c)
print('or:', a>b or b>c)
print('not:', not a>b)
print('not:', not b>c)
print(not True)
print(not False)
print()
