'''
print ("hello world")

print("testing connection with github")

letter = 'a'
result = []

tuple_sample = ['apple', 'banana', 'cherry']

for indx, item in enumerate(tuple_sample):
    if letter in item:
        result.append(indx)
    
print(result)
'''

# unit 2 practice 

x = 2.5
x= int(x)
print(x)
print (type(x))
print(float('2.5'))
smallest_value={'a':2,'b':1,'d':4, 'c':10}

print(min(smallest_value.keys())) # Evaluates to 'a'
#add or change value in the stored key
smallest_value['e'] = 5
print('modified dict with added \'e\' element', smallest_value)
#two ways to print a value (second is safer)
print('print value with []: ',smallest_value['a'])
print('print value with get.() method: ',smallest_value.get('f','not found'))

smallest_value.pop('a')
print('popping using dict.pop(key,default var) \'a\':\n',smallest_value,'\n')
keys = smallest_value.keys()
print('print keys using dict.keys():\n',keys,'\n')

values = smallest_value.values()
print('print values (dict.values()):\n',values,'\n')

items = smallest_value.items()
print('print all items in dict using dict.items():\n',items,'\n')

print('sorting dictionary using sorted(dict_name):\n',sorted(smallest_value))
