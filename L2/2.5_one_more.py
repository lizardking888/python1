my_list = [7, 5, 3, 3, 2]
number = 0
for i in my_list:
    i = int(input('type a number '))
    my_list.insert(number + 1, i)
    my_list.sort(reverse=True)
    print ('Внесено число ', i, 'Полный список ', my_list)
