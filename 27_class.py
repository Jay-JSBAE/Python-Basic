# chapter06_01
# 파이썬 클래스
# oop(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: #class Dog(object) object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성 -> 클래스가 초기화될때 무조건 쓰는 초기화 함
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화(설계도를 바탕으로 구현된것)
a = Dog("mikky", 2) #class명(name, age)
b = Dog("babd", 3)
c = Dog("babd", 3)

# 비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))
print()

if a.species == 'firstdog':
    print('{} is a {}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)
print('----------------------------------------------')

# 예제2
# self의 이해
class selfTest:
    def func1():
        print('func1 called')
    def func2(self):
        print('func2 called')

f = selfTest()
print(id(f))
#selfTest.func1() 예 # func1()은 클래스 메쏘드이기 때문
f.func2() # 메쏘드에 self가 있고 없고의 차이 / 클래스 메쏘드냐 인스턴스 메쏘드냐
print()

# 예제3
# 클래스 변수, 인스턴스 변수

class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 #재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)

del user1
print('After', Warehouse.__dict__)
print(Warehouse.stock_num)
print('----------------------------------------------')

# 예제4
class Dog2: #class Dog(object) object 상속
    # 클래스 속성
    species1 = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('Marry', 10)
# 메쏘드 호출
print(c.info())
print(d.info())
# 메쏘드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
