import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#반복문(while, for)
x = 1
while x < 10:
    print(x)
    x += 1

x = 1
while x < 10:
    print(x)
    x += 1
    y = 1
    while y < 10:
        print(y, end=' ')
        y += 1
