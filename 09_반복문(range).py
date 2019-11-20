#range(start:stop:step)
'''
1. 많은 데이터를 미리 준비하지 않아도 됨
2. 필요한 시점에만 데이터를 사용
'''

print(list(range(10)))
print(list(range(1,10,1)))
print(list(range(0,10,2)))
print(list(range(1,10,2)))
print(list(range(5,-5,-1)))
print(list(range(10,20)))

x = iter(range(10))
print(next(x))
print(next(x))
print(next(x))
