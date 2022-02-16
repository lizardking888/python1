a = int(input('введите число'))
b = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > b:
        b = a % 10
print ('самая большая цифра в числе', b)
