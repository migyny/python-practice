###############################    Session1          ###############################
#------------------------------  Problem set 1      --------------------------------

#1 
'''
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

count_mississippi(6)
'''
#2
'''
def swap_ends(my_str):
    if len(my_str) < 2:
        return my_str
    return "".join([my_str[-1], my_str[1:-1], my_str[0]])
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
'''

#3
