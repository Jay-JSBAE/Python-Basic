# chapter03_02
# 문자형(str)
# 문자형 중요

# 문자열 생성
str1 = "I am python"
str2 = 'python'
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 공백 포함 길이
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자 사용
print("I'm Boy") # 작은 따옴표떄문에 큰따옴표로
print('I\'m Boy') # 작은 따옴표안에 작은 따옴표를 쓴다면
print('a\tb') #tap
print('a\nb') # enter

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)
print()

# 탭, 줄 바꿈
t_s1 = "Click \t start!"
t_s2 = "New Line \n check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\python\test' #raw string을 이용하면 역슬러시 그대로 출력
print(raw_s1)
print()
