# coffes = [] # empty list
coffees = list()

coffees.append('아메리카노')
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인커피')
coffees.append('카페라떼')

count = len(coffees)
print('요소 개수 : %d' % count)

# 인덱싱
print('앞에서 2번째 음료 : %s' % coffees[2])
print('뒤에서 0번째 음료 : %s' % coffees[-1])

# 슬라이싱
print('전부 출력 : %s' % coffees[::])
print('1번째부터 3번째까지 음료 : %s' % coffees[1:4])
print('3번째부터 모든 음료 : %s' % coffees[3:])
print('맨앞부터 2번째까지 음료 : %s' % coffees[:3])

print('# 오름차순 정렬하기')
coffees.sort()
print(coffees)

print('# 내림차순 정렬하기')
coffees.sort(reverse=True)
print(coffees)

import random
random.shuffle(coffees)
print(coffees)
