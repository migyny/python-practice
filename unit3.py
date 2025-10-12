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


# ============================= Session 2 =============================
#------------------------------  Problem set 1      --------------------------------

#1
'''
#check if list is empty
#1. create a variable to store result
#2. loop through each item in the list
#3. convert each string to integer
#4. add number to created variable
#5. return our variable

def sum_of_number_strings(nums):

    if not(nums):
        return 0
    
    result = 0

    for num in nums:
        result += int(num)

    return result


nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
'''

#2 Problem 2: Remove Duplicates
'''
# Cases:
#no elements --> empty list
#no duplicate --> original list

#1. create empty set
#2. loop though the list of nums
#3. add every element to the set
#4. create a new list and loop through the set 
#5. add  element into the new list
#6. return the new list

def remove_duplicates(nums):

    result = set()
    new_list= []

    for num in nums:
        result.add(num)

    for num in result:
        new_list.append(num)

    return new_list

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
'''

#----------------------- other option----------
'''
def remove_duplicates(nums):
    return list(set(nums))

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
'''
#------other option--------
'''
# Q2: 

def remove_duplicates(nums):

    new_list = []
    
    for num in nums:
        if num not in new_list:
            new_list.append(num)
    
    return new_list

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))'''
#3
'''
#use isalpha() and enumerate while we loop through the string

#1. create a new list(for storing string)
#create dictionary (key: index, value: non character)
#2. loop through the original string (using enumerate)
#3. check for non characters (isalpha())
    #4. store the index of the non characters not(isalpha())
    #5. store non characters in the dictionary
    #6. add every alphabetical character of the string into a new list
#7. reversing the new list
#8. add non alphabetical values into the list
#9. list --> string --> return string

def reverse_only_letters(s):
    result = []
    non_characters= {}
    for indx, char in enumerate(s):
        if not char.isalpha():
            non_characters[indx]=char
        else:
            result.append(char)

    result.reverse()

    for indx,char in non_characters.items():
        result.insert(indx,char)
    return ''.join(result)
    

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
'''

#4 Longest Uniform Substring

# #create a dictionary (key: char, val:numb of occurences)

# #loop though the string
#     #dict[char] = dict.get(char, 1) + 1

# #return max(dictionary.values())

# def longest_uniform_substring(s):
#     new_dict={}

#     for char in s:
#         new_dict[char]= new_dict.get(char,1)+1

#     return max(new_dict.values())

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)

#5
def find_poisoned_duration(time_series, duration):
    count = 1
    for attack in range(min(time_series),max(time_series)):
        
        if attack in time_series:
            count+=duration
            

    return count



time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

#------------------------- Problem set 2-------------------

