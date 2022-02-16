print ('Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.')
def my_func(arg_1, arg_2, arg_3):
    arg_1 = int(input('Введите первое число: '))
    arg_2 = int(input('Введите второе число: '))
    arg_3 = int(input('Введите третье число: '))
    my_list = [arg_1, arg_2, arg_3]
    arg_max = max(my_list)
    my_list.remove(arg_max)
    arg_max2 = max(my_list)
    my_sum = arg_max + arg_max2
    return my_sum
print('Сумма двух наибольших чисел равна ', my_func(10, 40, 60))
    
    
