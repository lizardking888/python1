from math import factorial
n = int(input('Введите число: '))
fact = (a for a in range (1, n+1))
def my_gen():
    for el in fact:
        yield factorial(el)
g = my_gen()
for el in g:
    print (el)
