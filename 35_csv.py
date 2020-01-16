# chapter09_02
# csv 파일 읽기 및 쓰기

# csv : MEME - text/csv

import csv

# 예제1 - 콤마로 구분된 csv
# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.reader(f) # csv를 읽어올때는 reader
#     next(reader) # Header를 skip => 두번째 줄부터
    # #객체 확인
    # print(reader)
#
#     # 타입 확인
#     print(type(reader))
#
#     # 속성 확인
#     print(dir(reader)) #__iter__ 가있는거 확인 => for에서 사용 가능
#     print()
#
    # for c in reader:
    #     # print(c)
    #     print(' : '.join(c))
#
#         # 타입확인(리스트)
#         # print(type(c))
#         # list를 srt로
#         # print(' : '.join(c)) 이 경우 나라와 코드가 구분기호로 표시됨
#
# # 예제2 - | 로 구분된 csv
# with open('./resource/test2.csv', 'r') as f:
#     reader = csv.reader(f, delimiter='|') # 구분자 지정
#
#     for c in reader:
#         print(c)
#
# #예제3
# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.DictReader(f)
#
#     #확인
#     print(reader)
#     print(type(reader))
#     print(dir(reader))
#     print()
#
#     for c in reader:
#         print(c)
#
# 예제4
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('---------------------')

# # 예제5
# w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]
#
# with open('./resource/csv_write.csv', 'w', encoding='utf-8') as f:
#     wt = csv.writer(f)
#
#     # dir 확인
#     # print(dir(wt))
#     # 타입확인
#     # print(type(wt))
#
#     for v in w:
#         wt.writerow(v)

# # 예제6
# with open('./resource/csv_write1.csv', 'w', encoding='utf-8') as f:
#     # 필드명
#     fields = ['one', 'two', 'three']
#
#     # Dict writer
#     wt = csv.DictWriter(f, fieldnames=fields)
#     # header writer
#     wt.writeheader()
#
#     for v in w:
#         wt.writerow({'one':v[0], 'two':v[1], 'three':v[2]})
