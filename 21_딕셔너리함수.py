
a = {'name' : 'Bae', 'phone' : '01012345678', 'birth' : '860628'}
e = dict(
    Name = 'Jay',
    City = 'Seoul',
    Age = 34,
    Grade = 'A',
    Status = True
)
# dict_key, dict_values, dict_items : 반복문에서 사용 가능
print('e : ', e.keys()) # 키만 가져옴
#print('e : ', list(e.keys()))
print('e : ', e.values()) # 값만 가져옴
#print('e : ', list(e.values()))
print('e : ', e.items()) # 둘다 가져옴
#print('e : ', list(e.items()))
print('e : ', e.pop('City')) # pop은 값을 꺼내오는것(꺼내온 후 제거가 됨)
print('e : ', e)
print('e : ', 'Grade' in e)
print('e : ', 'City' in e)
print()
