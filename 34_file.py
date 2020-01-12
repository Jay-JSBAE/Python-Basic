# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('..'),  절대 경로('C:/')

# 파일 읽기(Read)
# 예제1
# open(경로, r or w or a (텍스트는 기본값이므로 rt로 안해도 됨), 인코딩(생략하면 기본적으로 utf-8))
f = open('./resource/text.txt', 'r', encoding='utf-8')
# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

# 모드 확인
print(f.mode)
print()

cts = f.read()
print(cts)

# 반드시 close
f.close()

# 예제2 => with문을 쓰면 close 라는 번거로움이 없음 내부적으로 close
with open('./resource/text.txt', 'r', encoding='utf-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
print()

# 예제3
# read(): 전체읽기, read(10) : 10 Byte (영문 기준)
with open('./resource/text.txt', 'r', encoding='utf-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20) # 다음 20Byte 마지막 읽은 위치를 기억하는 것
    print(c)
    f.seek(0,0) # 처음으로 돌아가는
    c= f.read(20)
    print(c)
print()

# 예제4
# read line : 한줄 씩 읽기
with open('./resource/text.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)
print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/text.txt', 'r', encoding='utf-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts: # 원문 형식으로 출력하고 싶을 때
        print(c, end='')
print()

# 파일 쓰기(write)
# 예제1 - 없는 파일을 가상으로 연결할때도 open
with open('./resource/text1', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/text1', 'a') as f:
    f.write('I love programming\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/text2', 'w') as f:
    list = ['Korea\n', 'Canada\n', 'USA\n']
    f.writelines(list)

# 예제4 - print 문이 파일로 출력
with open('./resource/text3', 'w') as f:
    print('Korea!', file=f)
    print('Canada!', file=f)
    print('USA!', file=f)
