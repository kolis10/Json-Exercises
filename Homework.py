# x = 'hello'

# if x == 'bye':
#     print('True')
# elif x == 'hello':
#     print('else if')
# else:
#     print('False')
#---------------------------------------------
# x = [1,2,3,4,5,6,7,8,9,10]

# for i in x:
#     if i == 3:
#         print(3)
#     else:
#         print('not 3')

# for i in x:
#     if i %2 != 0:
#         print(i)

# def is_even(a):
#     if a %2 == 0:
#         return True
#     else:
#         return False

# for n in x:
#     if is_even(n):
#         print(n)
# print(is_even(1))
# print(is_even(4))
# print(is_even(7))
# print(is_even(8))
#------------------------------------------
# def print_nums(a,b):
#     for i in a:
#         if b == 'even' and i %2 == 0:
#             print(i)
#         elif b == 'odd' and i %2 != 0:
#             print(i)

# def print_nums(a,b):
#     if b == 'even':
#         for i in a:
#             if i %2 == 0:     #This is the same as the top function
#                 print(i)
#     elif b == 'odd':
#         for i in a:
#             if i %2 == 0:
#                 print(i)
new_list = []
def add_nums_to_list(a,b):
    global new_list
    new_list = []
    for i in a:
        if b == 'even' and i %2 == 0:
            new_list.append(i)
        elif b == 'odd' and i %2 != 0:
            new_list.append(i)

x=[1,2,3,4]
y=[2,4,5,7,6]
z=[9,8,7,6]

add_nums_to_list(x, 'even')
print(new_list)
add_nums_to_list(y, 'odd')
print(new_list)
add_nums_to_list(z, 'even')
print(new_list)

# print_nums(x, 'even')
# print('---------------')
# print_nums(y, 'odd')
# print('---------------')
# print_nums(z, 'even')
#------------------------------------------
# x = [6,5,4]

# # write this function to add to x
# # def add(a):
# #     x.append(a)

# # add(7)
# # add('Issac')    
# # add(5)
# # print(x)

# # # delete from the end of the array of x
# def delete_end(a):
#     x.pop(a)


# # # delete from the beginning of the array x
# def delete_start():
#     x.pop(0)

# # print the whole list x
# printx()

# # print the index of x
# printx(2)

# #______________________________
# # write functions that do these same actions except you can pass an array
# y = []
# z = []
# def add(a,b):
#     a.append(b)

# def delete_end(a,b):
#     a.pop(b)

# add(y, 6)
# add(y, 7)
# add(y, 'asdf')
# add(y, 0)
# delete_end(y)
# delete_start(y)

# add(z, 6)
# add(z, 7)
# add(z, 'asdf')
# add(z, 0)
# delete_end(z)
# delete_start(z)


# obj = {}

# write function to add a key and a value to obj

# def add_to_dictionary(a,b,c):
#     c[a] = b
#     print(obj)

# add_to_dictionary('one', 1, obj)
# add_to_dictionary('name', 'john', obj)
# add_to_dictionary('age', 999, obj)

# remove a key with it's value from the dictionary
# delete_from_dictionary('name')
# delete_from_dictionary('age')
# #_______________________________________
# write a function that takes in an array and loops through it and prints only even numbers
# print_even([1,2,3,4])
# x = [9,8,7,6]

# # prints odds
# print_odd(x)

# #_______________________________________
# obj = {
#   'name': 'john',
#   'age': 45,
#   'address': False
# }

# # wirte a function that loops through the dictionary 'obj' and prints the keys or the values, depending what parameter was passed
# print_dictionary('keys')
# print_dictionary('values')

#---------------------------------------------------------------------------------------------------------------------------------------------------
# diction = {
#   'one': 1111,
#   'two': False,
#   'three': 33333,
#   'four': ['a','b','c',{
#       'name': 'Tom',
#       'age': 20,
#       'j': {
#         'sunny': 'sun',
#         'rain': 'cloud'
#       }
#     }]
# }

# for key, value in diction.items():
#   print(f'{key}: {value}')

# for value in diction.values():
#   print( value )

# for key in diction.keys():
#   print( key )

# for x in range(10):
#   print(x)

# for item in elst:
#   print( item )


# for index, item in enumerate(elst):
  # print(f'index: {index} is item: {item}')


# y = {
#   'one': 'x',
#   'two': True,
#   'three': 'john',
#   'four': 5
# }

# def print_dictionary(a, b, c):
#   print( a[b][c] )

# print_dictionary(x, 'four', 2)

# print x dict
# print_dictionary(x, 'three')
# print_dictionary(x, 'two')
# print_dictionary(x, 'four')

# # print y dict
# print_dictionary(y, 'four')
# print_dictionary(y, 'one')
# print_dictionary(y, 'four')


# def print_dictionary(r):
#   print( x[r] )

# print_dictionary('three')
# print_dictionary('two')
# print_dictionary('four')

# x = [0,0,0,0,0]

# def add(a, b):
#   x.insert(b, a)

# add(1, 2)
# add(2, 1)
# add('asdf', 0)
# add(4, 3)

# print(x)

# x = [1,2,3,4]

# x.append(5)
# x.insert(0, 5)

# print(x)


# def calculate(a, b, c=0):
#   print(a + b + c)

# calculate(b=0, a=5)
# calculate(1, 7, 6)
# calculate(b=2, a=9)

# def greet(a, b):
#   for x in args:
#     print(x)
#   print('--------')
  # print('hello ' + a + ', your last name is ' + b )
  # print(f'hello {args[0]}, your last name is {args[1]}')

# greet('joe', 'black')
# greet('pedro', 'flinstone','asdf','sadf')
# greet('shaq')
# # 'hello joe, your last name is black'

# x = 3
# y = 5

# print(x + y)