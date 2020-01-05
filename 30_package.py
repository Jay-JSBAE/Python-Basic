# Chapter06_3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 모듈을 모아놓은 폴더를 패키지라 할수 잇음
# __init__.py : python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용


# # 예제1
# import sub.sub1.mod_1 #uppend를 하지 않아도 이렇게 찾아가게 할수도 있음(sub 패키지 안에 sub1패키지 안에 module1)
# import sub.sub2.mod_2
#
# # 사용
# sub.sub1.mod_1.test1()
# sub.sub1.mod_1.test2()
# sub.sub2.mod_2.test3()
# sub.sub2.mod_2.test4()
# print()
# print()

# # 예제2
# # from 절 : 어디서부터 가져올껀데?
# from sub.sub1 import mod_1
# from sub.sub2 import mod_2 as t2 #alias 별명을 주는것
#
# mod_1.test1()
# mod_1.test2()
#
# t2.test3()
# t2.test3()
#
# print()
# print()

# 예제3
from sub.sub1 import * # 폴더에 있는거 다 가져오기
from sub.sub2 import *

mod_1.test1()
mod_1.test2()
mod_2.test3()
mod_2.test4()
