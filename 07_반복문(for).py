# for문
x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]

for i in x:
    print(i)

# for 문 중첩
# for i in x:
#     for j in y:
#         print('{} X {} = {}'.format(i,j,i*j))
# print()

#구구단
for i in range(2,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))
print()

# 예제 1
my_info = {
    "name" : 'Lee',
    "Age" : 34,
    "City" : "Seoul"
}

for k in my_info:
    print('key : ', k)
print()

for v in my_info.values():
    print('value : ', v)
print()

#예제2
#upper => 대문자 변환
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()
