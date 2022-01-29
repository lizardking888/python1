time = int(input('введите количество секунд'))
print ('Вы ввели ', time, 'секунд(ы)')
a = time % 60 #seconds
b = time // 60
c = b % 60 #minutes
d = time // 3600 #hours
print (f'{d}:{c}:{a}')
