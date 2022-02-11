stroka = str(input('type your sentence '))
print (stroka)
number = 1
word = 0
str1 = stroka.split()
for elem in str1:
    if len(str1[word]) < 10:
        print (f" {number}, {str1[word]}")
    else:
        print (f" {number}, {str1[word] [:10]}")
    number = number + 1
    word = word + 1



