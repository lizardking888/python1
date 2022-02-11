from functools import reduce
my_list = [elem for elem in range (100, 1001)]
def my_func (pr_el, el):
    return pr_el * el
print (reduce(my_func, my_list))
    
    
