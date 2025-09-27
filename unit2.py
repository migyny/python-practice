# -----------------Problem set 1--------------------

# all_in() function
#takes list of integers a and b 
#

      #             option A (faster)
'''
def all_in(a,b):
    if not(a):
        return True
    for val in a:
        if val not in b:
            return False
            
    return True


          #         option B (slower)
def all_in(a,b):

    if not (a):
        return True
    for num in a:
        found = False
        for nums in b:
            if num == nums:
                found = True
                break
            
        if found == False:
            return False
    return True

lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))
'''
#2
'''
#loop thorough both keys and values, adn populate the dictoinary

def create_dictionary(keys,values):

    result = {}
    for i in range(len(keys)):
        result[keys[i]]=values[i]
    return result

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

print(create_dictionary(keys,values))
'''
#3
'''
def print_pair(dictionary, target):

    if target in dictionary:       #!!!!!!!!!!!!
        print('Key: ', target)
        print("Value: ", dictionary[target])
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
'''
#4
'''
#find sum of keys and values
#if sum(keys)>sum(values) --> print "keys"
#if sum(values) > sum(keys) --> print "values"
#if they are equal --> print "balanced"
def keys_v_values(dictionary):
    keys =0 
    values = 0 
    for nums in dictionary:
        keys += nums
        values += dictionary[nums]
    if keys > values:
        return "keys"
    elif values > keys:
        return "values"
    else:
        return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum) 

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
'''
#5
'''
#current_inventory:  item:current stock
#restock_list:    item:quantity to be added
#if new item --> add to current_inventory
#return current_inventory

def restock_inventory(current_inventory,restock_list):

    for item in restock_list:
        current_inventory[item] = current_inventory.get(item,0)+restock_list[item]
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
result = restock_inventory(current_inventory,restock_list)
print(result)
'''
#6
'''
#create a dictionary for translating the grades to values
#
def calculate_gpa(report_card):

    grades = {
        "A":4, 
        "B":3,
        "C":2,
        "D":1,
        "F":0
    }
    return sum(grades.get(g,0) for g in report_card.values())/len(report_card)





report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
'''
#7
'''
#functoin returns a book with the highest rating
#create variable to store the rating
#loop through the dictionary#inside the for loop, check for the rating
#return dictionary with the highest rating

def highest_rated(books):
    highest_rating = 0
    best_book = None
    for book in books:
        if book["rating"] > highest_rating:
            highest_rating = book["rating"]
            best_book = book
    return best_book

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))
'''

#8
'''
def index_to_value_map(lst):

    dict_res = {}

    for idx, i  in enumerate(lst):
        dict_res[idx] = i

    return dict_res

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))
'''