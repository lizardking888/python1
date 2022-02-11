my_list = [90, 25, 29, 84, 11 ,58, 34, 28, 63, 72, 17, 345, 52, 78, 83, 2]
my_list2 = []
print ('Исходный список: ', my_list)
my_list2 = [my_list[index] for index in range (len(my_list)) if my_list[index] > my_list[index - 1]]
print ('Новый списoк ', my_list2)
