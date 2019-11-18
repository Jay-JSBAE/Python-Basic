import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''
# 형식 1
if(조건):
    사용될 구문

# 형식 2
if(조건):
    사용될 구문
if(조건):
    사용될 구문

# 형식 3
if(조건):
    사용될 구문
    if(조건):
        사용될 구문

# 형식 4
if(조건):
    사용될 구문
else:
    사용될 구문

# 형식 5
if(조건):
    사용될 구문
elif(조건):
        사용될 구문

# 형식 6
if(조건):
    사용될 구문
elif(조건):
        사용될 구문
else:
    사용될 구문
'''

# if
if True:
    print('실행될 문장 하나')
    if True:
        print('실행될 문장 둘')

if False:
    print('실행될 문장 셋')
