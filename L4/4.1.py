from sys import argv
script_name, time, salary, extra_pay = argv
print ('Расчёт зарплаты сторудника: ', script_name)
time = float('Введите выработку в часах: ')
salary = float('Введите значение ставки в час: ')
extra_pay = float('Введите премию: ')
def avr_salary():
    sal = time * salary + extra_pay
    return sal
print (avr_salary())
