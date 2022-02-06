number = int(input('введите количество элементов в списке '))
spisok = []
a = 0 #ограничить цикл
b = 0 #порядковый номер в списке
c = 1 # количество пар
spisok2 = []
while a < number:
    i = int(input('введи число'))
    spisok.append(i)
    a = a + 1
print (spisok)
while c <= number // 2:
    for q in spisok:
        q = spisok [b:b+2]
        q.reverse()
        spisok2.append(q)
        c = c + 1
        b = b + 2
        
print (sum(spisok2, []))
