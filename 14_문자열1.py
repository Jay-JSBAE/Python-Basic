# 문자형(str)

# 문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "how are you"
str_o4 = "seoul daejeon busan jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2) # 대문자 P
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print()

# 반복(시퀀스) : 순서가 있는 배열 형태
im_str = "Good Boy!"
print(dir(im_str)) # _iter_ 요게있으면 반복할 수 있다.
print()

# 반복(시퀀스)출력
for i in im_str:
    print(i)

print()
