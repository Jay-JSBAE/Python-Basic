# 문자형(str)

# 슬라이싱
str_sl = "Hello Python"
print(len(str_sl))
print()

# 슬라이싱 연습
print("-"*5 + "정방향" + "-"*5)
print(str_sl[0:5]) # 0부터 4-1 까지 나옴 (0,1,2,3만 나옴)
print(str_sl[6:12]) # 6부터 11-1 까지 나옴
print(str_sl[:len(str_sl)]) # str_sl[:12]
print(str_sl[:len(str_sl)-1]) # str_sl[:11]
print(str_sl[0:12:2]) # 1부터 9-1까지 2칸씩 나옴
print(str_sl[::2])
print("-"*5 + "역방향" + "-"*5)
print(str_sl[-5:]) # 뒤에서부터 -1, -2
print(str_sl[1:-2])
print(str_sl[::-1]) #역순으로 출력
print()

# 문자열 함수(upper, isalnum, startswith, count, endswith ...)
str_o1 = "python Nice"
str_02 = str_o1.upper() # 반대는 lower()
print("count : ", str_o1.count('b'))
print("Capitalize : ", str_o1.capitalize()) # 첫글자 대문자로 변환
print("endswith : ", str_o1.endswith("s")) # 마지막 문자가 무엇인지 체크
print("replace : ", str_o1.replace("Nice", 'Good'))
print("replace : ", str_o1.replace("thon", ' Good')) # 글자 변환
print("sorted : ", sorted(str_o1)) # 리스트 형태로 반환, 순서가 정렬되서 출력
print("split : ", str_o1.split(' ')) # 공백을 분리, !라면 !를 기준으로 분리
print("upper : ",str_02)
print()

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) # 문자를 아스키코드로
print(chr(122)) # 아스키 코드를 문자로
