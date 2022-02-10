month = int(input('Введите номер месяца '))
key1 = {3, 4, 5}
key2 = {6, 7, 8}
key3 = {9, 10, 11}
key4 = {12, 1, 2}
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
dict1 = dict(key1=seasons[1],key2=seasons[2], key3=seasons[3], key4=seasons[0])
print (dict1)
if month in key1:
    print(seasons[1])
    print(dict1.get('key1'))
if month in key2:
    print(seasons[2])
    print(dict1.get('key2'))
if month in key3:
    print(seasons[3])
    print(dict1.get('key3'))
if month in key4:
    print(seasons[0])
    print(dict1.get('key4'))
