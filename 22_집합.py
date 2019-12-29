# chapter03_6
# 집합(set) 특징
# 집합(set) 자료형(순서x, 중복x)

# 선언
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6])
d = set([1,2,3,4,4,4,4])
e = set([1,2,'Jay','Bae','Hello']) # 서로다른 자료형 저장 가능
f = {'Korea', 'Canada', 'England', 'France', 'Spain'} # 키가 없다면 set
g = {42, 'Jay', (1,2,3), 3.14159}

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)
print('e : ', type(e), e)
print('f : ', type(f), f)
print('g : ', type(g), g) # 중복 허용 안하기 때문에 4가 하나만
print()

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t : ', type(t),t)
print('t : ', t[0], t[1:3]) # 슬라이싱도 가능
print()

# 튜플 변환(set -> list)
l = list(c)
l2 = list(e)

print('l : ', l)
print('l2 : ', l2)
print()

# 길이
print(len(a))
print(len(b))
print(len(c))
print()

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2)) #교집합
print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2)) # 합집합
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2)) # 차집합
print()

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # 중복원소가 있는지 확인 false - 교집합 있다. true - 없다
print()

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # s1이 s2의 부분 집합이냐
print('superset : ',s1.issuperset(s2)) # s1이 s2를 포함하는 집합이냐
print()

# 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print('s1 : ', s1)
s1.remove(3)
print('s1 : ', s1)
s1.discard(7)
print('s1 : ', s1) #집합에서 에러없이 출력하고플때 discard => 없는 원소를 삭제할때
s1.clear()
print(s1)
