my_list = [7, 5, 3, 3, 2]
number = 0
for i in my_list:
    i = int(input('type a number '))
    if i == my_list[number]:
        my_list.insert(number + 1, i)
        print ('Внесено число ', i, 'Полный список ', my_list)
    elif i > my_list[number]:
        my_list.insert(0, i)
        print ('Внесено число ', i, 'Полный список ', my_list)
    if my_list[-1] < i < my_list[number] :
        my_list.insert(number + 1, i)
        my_list.sort(reverse=True)
        print ('Внесено число ', i, 'Полный список ', my_list)
    if i < my_list[-1]:
        my_list.append(i)
        print ('Внесено число ', i, 'Полный список ', my_list)
