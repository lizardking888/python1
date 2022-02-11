# 4.6.1

print ('итератор, генерирующий целые числа, начиная с указанного:')
print ('итератор будет работать с числа 3 ')

from itertools import count, cycle

for el in count (3):
    if el > 10:
        break
    else:
        print (el)
#итератор, повторяющий элементы некоторого списка, определённого заранее

my_list = list(input('введите список:'))
i = 0
for elem in cycle(my_list):
    if i>15:
        break
    else:
        print(elem)
        i = i + 1
