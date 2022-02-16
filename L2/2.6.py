общий = []
my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
dict1= {}
анализ = {}
while input('Добавить продукт? Введите да/нет: ') == 'да':
    number = int(input('Введите порядковый номер товара: '))
    name = input('Введите название товара: ')
    my_list1.append(name)
    key1 = 'название'
    dict1[key1] = name
    анализ[key1] = my_list1
    
    price = input('Введите цену товара: ')
    my_list2.append(price)
    key2 = 'цена'
    dict1[key2] = price
    анализ[key2] = my_list2
    
    ammount = input('Введите количество товара: ')
    my_list3.append(ammount)
    key3 = 'количество'
    dict1[key3] = ammount
    анализ[key3] = my_list3

    units = input('Введите единицы товара: ')
    my_list4.append(units)
    key4 = 'ед'
    dict1[key4] = units
    анализ[key4] = my_list4
    
    print(dict1)

    общий.append(tuple([number, dict1]))
print ('Общий список по первому подпункту задания: ', общий)
print ('Список аналитики: ', анализ)

