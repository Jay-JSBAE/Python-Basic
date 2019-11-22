# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
srt : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

str1 = "python"
bool = True
str2 = "Anaconda"
float = 10.0  # 10 == 10.0 은 false
int = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9) # 괄호 생략 가능 tuple = 7,8,9
set = {5, 8, 9}

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))
