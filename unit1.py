# -----------SECTION 1/session 1------------------------
#1
'''
def hello_world():
    print("Hello, world!")

hello_world()
'''
#2
'''
def todays_mood():
    mood = "🥱"
    print("Today's mood: " + mood)

todays_mood()
'''
#3
'''
def print_menu(menu):
    print("Lunch today is: " + menu)


print_menu("🍔")
'''
#4
'''
def sum(a, b):
    return a + b

#sum(a,b)  
#sum(sum(a,b),sum(a,b))
#result = sum(a,b)
#sum(result,result)

result = sum(13,27)
print(sum(result,result))
'''
#5
'''
def product(a,b):
    return a * b

print(product(22,7))
'''
#6
'''
#if age <18 --> child
# if age =>18 --> adult

def classify_age(age):
    if age<18:
        return "child"
    else:
        return "adult"
    
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
'''

#7
'''
#if hour == 2 --> "taco time 🌮"
#elif hour == 12 --> "peanut butter jelly time 🥪”
#else --> "nap time 😴"

def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"
    
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)
'''

#8
'''
#input can be any number
# if score == 21 --> "Blackjack!
# #elif score > 21 --> "Bust!"
# elif score >= 17 and score <21 --> "Nice hand!"
#else --> "Hit me!"
def blackjack(score):
    if score == 21:
        return "Blackjack!"
    elif score > 21:
        return "Bust!"
    elif score >= 17 and score < 21:
        return "Nice hand!"
    else:
        return "Hit me!"
    
print(blackjack(21))
print(blackjack(24))
print(blackjack(19))
print(blackjack(10))
'''
#9
'''
#case 1: list present --> return the item
#case 2: list empty --> return "empty"
#check the length of the list, if the length is 0, return "empty"
#otherwise return the first item in the list

def get_first(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[0]
    
list1 = [2,3]
print(get_first(list1))
'''
#10
'''
#list has more than one element --> return last element of the list
# list has no parameters --> return none

def get_last(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[-1]
    
list1 = [1]
print(get_last(list1))
'''
#11
'''
# use range (1,stop+1)
#if value less tan 0 --> none
def counter(stop):
    if stop <= 0:
        return None
    else:
        for i in range(1,stop+1):
            print(i)

counter(10)
'''
#12
'''
def sum_ten():
    total = 0
    for i in range(1,11):
        total += i
    return total

print(sum_ten())
'''
#13
'''
# if the stop value is less than 1, return none

def sum_positive_range(stop):
    if stop < 1:
        return None
    else:
        total = 0
        for i in range(1,stop+1):
            total += i
        return total
    
print(sum_positive_range(10))
'''
#14
'''
def sum_range(start,stop):
    if start > stop:
        return None
    else:
        total = 0
        for i in range (start,stop+1):
            total +=i
        return total
    
print(sum_range(3,9))
'''
#15
'''
def print_negatives(lst):
    for i in lst:
        if i < 0:
            print(i)

print(print_negatives([1,2,3,4,-5]))
'''
# --------------------section 2------------------------
#1
'''
def greet_user(name):
    print("Hello " + name)

greet_user('Andrew')


'''
#2
'''
def difference(a,b):
    return a-b

diff = difference(8, 3)
print(diff)
'''
#3
'''
# function creates new list 'ans' (length = 2n),
# where n=length of priginal list 
#
def concatenate_list(nums):
 #
 #   if not(nums):
 #       return None
 #   n = len(nums)
 #   ans = [0] * (2*n)
 #   for numbers in range(n):
 #       ans[numbers] = nums[numbers]
 #       ans[numbers+n] = nums[numbers]
    #or
    ans= 2*nums
    return ans

lst = [1,2,3,4]
print(concatenate_list(lst))
'''
# 4
'''
def sleep_assessment(hours):
    if not isinstance(hours,int):
        print("Error")
        return
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours <= 10:
        print ("You got a good night's rest!")
    else:
        print("You're a sleep prodigy!")

sleep_assessment('a')
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)
'''
#5
'''
# if you return 10% --> *0.1

def calculate_tip(bill,service_quality):
    if service_quality == 'poor':
        return bill *0.1
    elif service_quality == 'average':
        return bill * 0.15
    elif service_quality == 'excellent':
        return bill *0.2
    else:
        return None
    
tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
'''
#6
'''
#we can only check all conditions for player1:
#if he has a winning hand, he wins
#in all other cases, player 2 wins
#edge cases: uppercase letters, not a valid input (rock,paper,scissors)
def rock_paper_scissors(player1,player2):
    player1 = player1.lower()
    player2 = player2.lower()
    valid_choices = ['rock','paper','scissors']
    if player1 not in valid_choices or player2 not in valid_choices:
        print('Invalid input')
        return
    elif player1 == player2:
        print ("It's a tie!")
    elif player1 == 'rock' and player2 == 'scissors':
        print ("Player 1 wins!")
    elif player1 == 'scissors' and player2 == 'paper':
        print ("Player 1 wins!")
    elif player1 == 'paper' and player2 == 'rock':
        print ("Player 1 wins!")
    else:
        print("Player 2 wins!")

    

rock_paper_scissors("1a", "rock")
rock_paper_scissors("scissors", "ROCK")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")
'''
#7
'''
def halve_lst(lst):
    result =[]
    for number in lst:
        halved = number//2
        result.append(halved)
    return result


print(halve_lst([2,4,6,8]))
'''
#8 already did it

#9
'''
#edge cases: if m<n --> none
def countdown(m,n):
    if  m < n:
        return None
    
    for count in range(m,n-1,-1):
        print (count)

countdown(5,5)
'''

#10
'''
#takes two integers base and exponent

def power(base,exponent):
    return base**exponent


pow1 = power(1,5)
print(pow1)
'''

#11
'''
def list_length(lst):
    count = 0
    for i in lst:
        count+=1
    return count

lst = [2,4,6,8,10]
length = list_length(lst)
print(length)
'''

#12


# -----------------Session 2/section 1----------------
#1
'''
#  if list is empty --> return none
#use the for loop to iterate through the list

def print_list(lst):
    for item in range(len(lst)):
        print(lst[item])


lst1 = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst1)
'''

#2,3
'''
# edge cases:
#if list is empty --> none

# pseudo code

#func doubled()
#use range function to loop through the list
#multiply each element in the list by 2
#print the value

def doubled(lst):
    lst2=[]
    for num in lst:
        lst2.append(num*2)
    return lst2

lst1 = [-1,-2,3]
print(doubled(lst1))
'''

#4
'''
def flip_sign(lst):
    new_list=[]
    for i in range(len(lst)):
        new_list.append(-lst[i])
    
    return new_list


lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
'''

#5
'''
# find a maximum and minimum value
#substract minimum from maximum
#return the result

def max_difference(lst):
    if not(lst):
        return None
    max_val = max(lst)
    min_val = min(lst)
    return max_val - min_val

lst = [1,2,3]
max_diff = max_difference(lst)
print(max_diff)
'''

#6
'''
# if the list is empty or other data type --> none
def count_less_than(numbers, threshold):
    if not(numbers):
        return None
    counter = 0;
    for num in numbers:
        if num > threshold:
            counter +=1
    return counter

numbers = [12,8,2,4,4,10]
counters = count_less_than(numbers,15)
print(counters)
'''
#7
'''
#iterate through the list and check if it is divisible by 2

def get_evens(lst):
    lst2=[]

    for num in lst:
        if num % 2 == 0 :
            lst2.append(num)
    return lst2
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)
'''
# 8 ----------------------!--------------
'''
#use range function (5,101, 5)
#prints numbers that are multiples of 5 from 5 to 100

def multiples_of_five():
    for i in range(5,101,5):
        print(i)    

multiples_of_five()

'''

#9
'''
def find_divisors(n):
    lst2=[]
    for i in range(1,n+1):
        if n % i == 0:
            lst2.append(i)
    return lst2

lst = find_divisors(6)
print(lst)
'''

#10


#11
'''

def print_indices(lst):
    for i in range(len(lst)):
        print (i)


lst = [5,1,3,8,2,0]
print_indices(lst)
'''

#12
'''
#if target is found --> return index of target
# if not found --> -1

def linear_search(lst,target):

    for num in range(len(lst)):
        if lst[num] == target:
            return num
    return -1

lst = [1,4,5,2,8]
position = linear_search(lst,8)
print(position)
'''

