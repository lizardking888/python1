my_dict = dict(one='один', two= 'два', three= 'три', four= 'четыре')
print (my_dict)
final_file = []
my_obj = open ('py5.4.txt')
for line in my_obj:
    line = list(line.split())
    print(line)

    if line[0] in my_dict:
        number = my_dict.get(line[0])
        final_file.append(number + line[1] + line[2])
print(final_file)
input_file = open('input_file_5.4.txt', 'w')
input_file.writelines(final_file)
input_file.close()

