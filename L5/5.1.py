my_file = open('out_file.txt', 'w')
while True:
    line = input('введите то, что надо записать:')
    my_file.write(line)
    if line == '':
        break
my_file.close()
