# chapter03_03
# 문자형(str)
# 문자형 중요

# 멀티라인 입력
# 역슬러시 사용
multi_str = \
"""
string
multi line
test
"""
print(multi_str)
print()

# 문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "how are you"
str_o4 = "seoul daejeon busan jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2) #대문자 P
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print()

# 문자열 함수(upper, isalnum, startswith, count, endswith ...)
print("Capitalize : ", str_o1.capitalize()) # 첫글자 대문자로 변환
print("endswith : ", str_o2.endswith("s")) # 마지막 문자가 무엇인지 체크
print("replace : ", str_o1.replace("Nice", 'Good'))
print("replace : ", str_o1.replace("thon", ' Good')) # 글자 변환
print("sorted : ", sorted(str_o1)) # 리스트 형태로 반환, 순서가 정렬되서 출력
print("split : ", str_o4.split(' ')) # 공백을 불리, !라면 !를 기준으로 분리
print()

# 반복(시퀀스) : 순서가 있는 배열 형태
im_str = "Good Boy!"
print(dir(im_str)) # _iter_ 요게있으면 반복할 수 있다.
print()

# 반복(시퀀스)출력
for i in im_str:
    print(i)

print()
