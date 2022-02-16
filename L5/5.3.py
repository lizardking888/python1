my_obj = open('py5.3.txt')
salary_overall = []
my_list_down = []
number = len(my_obj.readlines())
my_obj = open('py5.3.txt')
for my_list in my_obj:
    my_list = my_list.split()
    salary = float(my_list[1])
    salary_overall.append(salary)
    if salary < 20000:
        my_list_down.append(my_list)
print ('Сотрудники, которые получают меньше 20000: ', my_list_down)
avr_salary = sum(salary_overall) / number
print ('Средняя заработная плата составляет:', avr_salary )
    


