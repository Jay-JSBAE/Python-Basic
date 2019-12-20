# 튜플 함수
a = (5,2,3,1,4)
print('a =', a)
print('a = ', a.index(3)) #숫자3의 위치가 어디냐
print('a = ', a.count(2)) #숫자2의 개수가 몇개냐

# 팩킹 & 언팩킹 (packing and unpacking)
print('>>>>>>')
# 팩킹
t = ('Korea', 'Canada', 'England', 'France')
print(t)
print(t[0])
print(t[-1])

# 언팩킹 => 묶여있떤걸 풀어서 각각 원소에 대입
print('>>>>>>')
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
print('>>>>>>')
t2 = 1,2,3 #괄호가 없어도 튜플
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
