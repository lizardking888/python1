my_file = open('file_5.5.txt', 'w')
numbers = input('Введите числа:')

my_sum = 0
num = 0
input_numbers = numbers.split()
str_input_numbers = ' '.join(input_numbers)
print (str_input_numbers)
for i in input_numbers:
    my_sum = my_sum + int(input_numbers[num])
    num = num + 1
print (my_sum)
my_file.writelines(str_input_numbers)
my_file.close()
