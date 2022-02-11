print ('Соберем данные о пользователе ')
def my_func():
    name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    year = input('Введите год своего рождения: ')
    city = input('Укажите город проживания: ')
    email = input('Укажите адрес Вашей электронной почты: ')
    tel = input('Укажите номер Вашего телефона: ')
    return name, last_name, year, city, email, tel
print (my_func())
