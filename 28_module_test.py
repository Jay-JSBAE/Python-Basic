import sys
# print(sys.path)
# print(type(sys.path))
sys.path.append('I:\Python\math') # 경로 삽입 요게 중요

# print(sys.path)
#
# import test_module
#
# # 모듈 사용
# print(test_module.power(10, 3))

# test_module에 있는 print문이 실행되지 않게 하려면?
# 불필요한것들이 출력되지 않게 하려면?
# __name__ 사용

#import chapter06_02
import mod
print(mod.add(10,2))
