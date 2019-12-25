# chapter03_5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서 x, 키 중복x, 수정o, 삭제o)

# 선언의 방법(키 : 값)
a = {'name' : 'Bae', 'phone' : '01012345678', 'birth' : '860628'}
b = {0 : 'Hello Jay',}
c = {'arr' : [1,2,3,4]} #키만 존재한다면 값은 어떤 형식으로든 상관없음
d = {
    'Name' : 'Jay',
    'City' : 'Seoul',
    'Age' : 34,
    'Grade' : 'A+',
    'Status' : True
}
e = dict(
    Name = 'Jay',
    City = 'Seoul',
    Age = 34,
    Grade = 'A',
    Status = True
)# dict 안에 튜플 형식으로!

# 출력
print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)
print('e : ', type(e), e)
print()

# 원하는 키로 출력
print(e.get('Name'))
print(e.get('Address'))
#print(['Address']) # 키가 존재하면 출력되나, 존재하지 않으면 에러가 표시됨
#print(e[0]) # 키가 0인것
print(e.get(0))
print(e.get('City'))
print(e.get('Age'))
print(e.get('Grade'))
print()

# 딕셔너리 추가,수정 => 원래 있던 키에 추가하면 업데이트 해버림
e['phone'] = '01011112222'
print('e : ', e)
print()

e['Name'] = 'Bae'
print('e : ', e)
print()

e.update(City='Busan')
print('e : ', e)
print()

temp = {'Grade' : 'B'}
e.update(temp)
print('e : ',e)



# 키의 개수 세기
print('a : ', len(a))
print('b : ', len(b))
print('c : ', len(c))
print('d : ', len(d))
print('e : ', len(e))
print()
