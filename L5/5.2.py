my_file = open('py5.2.txt')
content = my_file.readlines()
print (content)
length = len(content)
print ('Количество строк:', length)
my_file = open('py5.2.txt')
full_content = my_file.readlines()
a = 0

for i in range(len(full_content)):
    my_str = full_content[a].split()
    print (my_str)
    if a < length:
        a = a + 1
        print ('Количество слов в', a, 'строке:', len(my_str))
    else: break

