import json

# empty_var = {}

# with open('users.json', 'r') as jfile:
#     empty_var = json.load(jfile)
# print(empty_var)

# with open('users.json', 'r') as j: #you don't need to make an empty_var, just print
#     print(json.load(j))
 
with open('users.json', 'r') as j:
    jfile = json.load(j)

for d in jfile:
    print( d['first_name'])
