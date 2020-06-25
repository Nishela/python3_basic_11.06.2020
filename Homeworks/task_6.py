'''6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.'''

# a)
from itertools import count

print('Вариант а)')
for itm in count(1):
    if itm > 15:
        break
    print(itm, end=' ')

# б)
from itertools import cycle

print('\nВариант б)')
user_list = [300, 2, 12, 44, 78, 123, 55]
cnt = 0
for itm in cycle(user_list):
    if cnt > 10:
        break
    print(itm, end=' ')
    cnt += 1