# chapter03_02
# 문자형(str)
# 문자형 중요

# 슬라이싱
str_sl = "Hello Python"
print(len(str_sl))
print()

# 슬라이싱 연습
print(str_sl[0:5]) # 0부터 3-1 까지 나옴 (0,1,2만 나옴)
print(str_sl[6:12]) # 6부터 11-1 까지 나옴
print(str_sl[:len(str_sl)]) # str_sl[:12]
print(str_sl[:len(str_sl)-1]) # str_sl[:11]
print(str_sl[0:12:2]) # 1부터 9-1까지 2칸씩 나옴
print(str_sl[::2])
print(str_sl[-5:]) # 뒤에서부터 -1, -2
print(str_sl[1:-2])
print(str_sl[::-1]) #역순으로 출력
print()

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) # 문자를 아스키코드로
print(chr(122)) # 아스키 코드를 문자로
