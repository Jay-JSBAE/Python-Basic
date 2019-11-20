# break
# 예제1
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 7:
        print('Found : 7!')
        break
    else:
        print('Not found : ', num)
print()

# 예제2
x = 1
while x < 10:
    if x == 5:
        break
    print('good job')
    x += 1
print('end')

# 예제3
for i in range(10):
    if i ==5:
        break
    print('good job')
print('for end')

# continue
for i in range(101):
    if i % 2 == 0:
        continue #다시 조건문으로 이동 (밑에 실행안함)
    print(i)
else:
    print('good job')
print()

m = 5
while m > 0:
    m -=1
    if m ==2:
        continue
    print(m)
print('Loop Ended')
print()
