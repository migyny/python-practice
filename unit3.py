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
'''
#1. create dictionary, where letter = key
#2 store each letter in the dictionary by looping through the string
#check the length of dictionary: if less than 26 --> false
#else -->true
def is_pangram(my_str):
    my_dict= {}
    for char in my_str:
        my_dict[char]=True
    if len(my_dict) >= 26:
        return True
    return False


my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

'''


#----------------------Problem Set 2---------------

#5


#Goal: count apperance of each character

#Takes string as a parameter and returns the original string

#implementation:
#
#loop through the string
#initialize variable to count instances of a character
#loop through the string
#if we see different letter --> :
#   create a string and add a leeter and its instance
#   reset the counter
#if len(original string)< result:
#   return original string

#return the new string
'''
def compress_string(my_str):
    counter = 1
    str_result= ""
    for char in range(1,len(my_str)):

        if my_str[char] == my_str[char-1]:
            counter+=1
        else:
            str_result += my_str[char-1] +str(counter)
            counter = 1
            
    str_result +=my_str[char]+str(counter)
    if len(my_str) < len(str_result):
        return my_str
    
    return str_result
        

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)
'''

#6
'''
def find_the_needle(haystack,needle):

    return haystack.find(needle)

    

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))
'''