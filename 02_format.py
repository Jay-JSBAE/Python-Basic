name = 'jay'
age = 100
n = 888888888888.888888
print('My name is %s. My age is %d.' %(name,age)) # 많이 쓰지 않음
print('My name is {}. My age is {}.' .format(name,age))
print('My name is {0}. My age is {1}.' .format(name,age)) #0번째 입력
print()


print('{} X {} = {}'.format(2,3,6))

# 0번째 1번째 2번째 4자리씩 써
print('{0:4} X {1:4} = {2:4}'.format(2,3,6)) #오른쪽 정렬
print('{0:<4} X {1:<4} = {2:<4}'.format(2,3,6)) #왼쪽 정렬
print('{0:.3f}'.format(1/4.0))
print('{0:.4f}'.format(1/4.0))
print()

#컴마 삽입
print('{0:,.3f}'.format(n))
print()

name1 = 'jason'
age1 = 20

# 15자리에 맞춰서 중앙정렬을 해라
print('{0:^15}'.format(name1))
# 왼쪽 정렬
print('{0:<15}'.format(name1))
#오른쪽 정렬
print('{0:>15}'.format(name1))
