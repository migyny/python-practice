class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# return the last node in the cycle 
#if no cycle -> reutrn none

#plan
#slow = fast = head
#while loop 
#


def find_last_node_in_cycle(head):
    if not head or not head.next:
        return None
    
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else: 
        return None
    
'''
Find the start of the cycle.
Move one pointer back to head.
Move both one step at a time.
When they meet again, that node is the start of the cycle.
Find the node whose .next points to the start of the cycle.
From the start node, traverse the cycle until current.next == start.
That current node is the last node in the cycle.
Return that node.
# Step 3: Find the start of the cycle
    slow = head  # move one pointer to head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    start_of_cycle = slow

    # Step 4: Find the node just before the start of cycle
    current = start_of_cycle
    while current.next != start_of_cycle:
        current = current.next

    # Step 5: Return that last node
    return current
'''

            
    
            
    
        
    

num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num4=Node("num4")
num1.next = num2
num2.next = num3
num3.next = num4
num4.next= num2

print(find_last_node_in_cycle(num1))





















# def is_circular(head):
#     if not head:
#         return False

#     current_num = head.next
#     while current_num:
#         if current_num.next == head:
#             return True  
#         current_num = current_num.next
#     return False

# num1 = Node("num1")
# num2 = Node("num2")
# num3 = Node("num3")
# num1.next = num2
# num2.next = num3
# num3.next = num1
# print(is_circular(num1))

# var1= Node("var1")
# var2= Node("var2")
# var3= Node("var3")
# var1.next = var2
# var2.next=var3
# print(is_circular(var1))

