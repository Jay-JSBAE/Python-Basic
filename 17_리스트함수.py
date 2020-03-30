# 리스트 함수
print('>>>>')
a = [5, 2, 3, 1, 4]
print('a - ', a)

print(a.index(3))

a.append(6) #append 함수는 마지막 끝에 추가
print(a)

a.insert(2,7) #2번째 위치에 7을 넣을꺼야.
print(a)

ex = [8,9]
a.extend(ex) # 끝에 추가
print(a)

a.sort() #오름차순 정렬
print(a)

a.reverse() #내림차순 정렬
print(a)

# 삭제 : remove, pop, del
del a[1]
print(a)

a.remove(7) # 제거할 값을 넣기 = del a[2] => 이경우는 데이터가 적을때
print(a)

print('a = ', a)
print(a.pop()) #pop은 마지막 원소를 꺼내오는것
print(a)

print(a.count(4)) # 리스트에서 4의 개수가 몇개냐
print(a)
print('>>>>>')

# 반복문 활용 (끝부분부터 꺼내오기)
while a:
    data = a.pop()
    print(data)
