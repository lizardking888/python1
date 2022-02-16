my_dict = {}
my_file = open ('py5.6.txt')
for line in my_file:
    line = line.split()
    num = len(line)
    for my_sum in line:
        my_sum = 0
        i = 1
        while i < num:
            my_sum = my_sum + int(line[i])
            i = i + 2
    my_dict.update({line[0]: my_sum})
print (my_dict)
        
        
        
