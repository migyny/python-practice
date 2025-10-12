###############################    Session1          ###############################
#------------------------------  Problem set 1      --------------------------------

#1
'''
# loop through the number --> if n % i ==0 --> False 

def is_prime(n):
    if n < 1:
        return False
    
    for i in range(2,n//2):
        if n % i == 0:
            return False
        
    return True
 #36: 2,3,6,13,12

print(is_prime(5))
print(is_prime(12))
print(is_prime(7))
'''

#2 Two-Pointer reverse list
'''
#plan

#pointer left = 0, pointer right = len(lst)-1
#iterate trough the list (while left<right)
    # left,right = right,left
    # left +=1   right -=1


def reverse_list(lst):

    if not(lst):
        return lst
    
    left = 0
    right = len(lst)-1

    while left < right:
        lst[left],lst[right]= lst[right],lst[left]
        left +=1
        right -=1

    return lst


lst = [1,2,3,4,5,6]
print(reverse_list(lst))
'''



#4
'''
#pointer left = 0, pointer right = len(lst)-1
#iterate trough the list (while left<right)
    # if the left is odd and right even
        #swap left and right 
        # right -=1
        # left +=1
    #elif left is even 
        #left +=1
    #elif right is odd
        #right -=1

def sort_array_by_parity(nums):

    if len(nums)<2:
        return nums
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] %2 != 0 and nums[right] %2 == 0:
            nums[left],nums[right] = nums[right],nums[left]
            left +=1
            right -=1
        elif nums[left] % 2 == 0:
            left +=1
        elif nums[right] % 2 != 0:
            right -=1

    return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
'''

