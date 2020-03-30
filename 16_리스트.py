# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = [] #빈 리스트 선언
b = list() #빈 리스트 선언
c = [70, 75, 80, 85] # 0 ~ 3까지 4개의 원소를 가지고 있음ㅁ
d = [1000, 10000, 'Jay', 'Bae', 'python']
e = [1000, 10000, ['Jay', 'Bae', 'python']]
f = [11.21, 'Hello', 2, 3, False, 3.14159]

# 인덱싱 - 원하는 데이터를 꺼내오는 과정
print('>>>>>')
print('d -', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) # base는 문자열이기 때문에 형변환

# 슬라이싱
print('>>>>')
print('d - ', d[0:3]) # 0부터 3개 나와라
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산 list + list = list
print('>>>>')
print('c + d = ', c + d)
print('c * 3 =', c * 3)
print("'Test' + c[0] = ", 'Test' + str(c[0])) #70은 숫자이므로 문자로 형변환

# 값 비교 - 참고
print('>>>>>')
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# identity(id) - 참고
print('>>>>>')
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
#c = [70, 75, 80, 85]
print('>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # c[1:2] = c[1]
print('c -', c)
c[1:3] = []
print('c -', c)

# 리스트 제거
del c[2]
print(c)
