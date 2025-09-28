#######################################   Session 1 #######################################
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

# -------------------------Version Set 2-------------------

#1

# Steps:
# create 2 boolean variables to store inc/decr order
#loop through the list 
# #check if the current number < next number or curr_num > next_num
#return flase if pattern breaks

#pseudo code
'''
func is_monotonic(nums)

increasing = false
decreasing = false    

    for indx,num in enumerate(nums[0:-1])

        if num => num+1
            increasing = true
        else
            increasing = false
        
        if num <= num+1
            decreasing = true
        else
            decreasing = fasle

return increasing or decreasing  

end
'''
'''
def is_monotonic(nums):

    increasing = True
    decreasing = True  

    for indx in range(len(nums)-1):

        if nums[indx] != nums[indx+1]:

            if nums[indx] > nums[indx+1]: #increasing
                decreasing = False
        
            if nums[indx] < nums[indx+1]: #decreasing
                increasing = False
        

    return increasing or decreasing
    

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))
'''
#2
'''
def student_directory(student_names):

    student_id = {}

    for indx, student in enumerate(student_names):
        student_id[student] = indx+1
        
    
    return student_id

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))
'''

#3 
'''
def get_description(info, keys):
    for key in keys:
	    print(info.get(key, None))
          
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
'''
#4
'''
def sum_even_values(dictionary):
    sums = 0
    for num in dictionary.values():
        if num % 2 == 0:
            sums +=num
    return sums

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
'''

#5
'''
#if we have new proce for rpoduct in catalog2
#assign price in catalog2 to catalog1
def merge_catalogs(catalog1,catalog2):

    for product in catalog2:

        catalog1[product]= catalog2[product]

    return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1,catalog2))
'''
#6
'''
def get_items_to_restock(products,restock_threshold):

    items_restock =[]

    for items in products:
        if restock_threshold > products[items]:
            items_restock.append(items)



    return items_restock

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products,restock_threshold))
'''
#7
'''
def most_popular_genre(movies):

    genre_ratings = {}
    for movie in movies:

        genre = movie["genre"]
        rating = movie["rating"]
        if genre in genre_ratings:
            genre_ratings[genre]["total"] +=rating
            genre_ratings[genre]["count"] +=1
        else:
            genre_ratings[genre] = {"total":rating, "count":1}

        max_avg =-1
        best_genre = None
        for genre, data in genre_ratings.items():
            avg_rating = data['total'] / data['count']
            if avg_rating > max_avg:
                max_avg = avg_rating
                best_genre = genre

    return best_genre

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))
'''

#8
'''
def quality_control(product_scores,threshold):

    new_dict = {}

    for product in product_scores:

        if product_scores[product] >= threshold:
            new_dict[product] = "pass"
        else:
            new_dict[product] = "fail"

    return new_dict

product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))
'''
