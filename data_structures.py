# # lists in python are like arrays in ruby
# a_list = ["Frog", "Toad", "Newt"]

# print(a_list[0])
# a_list[1]
# print(a_list[2])
# print(len(a_list))
# if "Frog" in a_list:
#   print("Woo Frogs!")

# #tuples in python cant be changed
# my_tuple = ('I', 'am', 'fond', 'of', 'Python')
# print(my_tuple[2])
# print(len(my_tuple))

# k, m, s = 1, 2, 3
# print(m)
# print(s)
# print(k)

# #dictionaries are like hashes in ruby
# my_dict = { 'Kyrsten': 'Frog', 'age': 17, 'food': 'gingerbread' }
# print(my_dict['Kyrsten'])
# print(my_dict['food'])
# if 'age' in my_dict:
#   print(f"the edge of {my_dict['age']} ")

from lib2to3.pytree import LeafPattern


my_list = ["Frog", "Toad", "newt"]
print(my_list)
my_list.insert(1, 'Salamander')
print(my_list)
my_list.append("Frog")
my_list.append("newt")
my_list.append("Frog")
print(my_list.count("Frog"))
# does something cool but not what challenge asked for
# counter = { 'Frog': my_list.count('Frog'), 'Toad': my_list.count('Toad'), 'newt': my_list.count('newt'), 'Salamander': my_list.count('Salamander') }
counter = {}
for each_item in my_list:
  lowercase_animal = each_item.lower()
  if lowercase_animal in counter:
    counter[lowercase_animal] = counter[lowercase_animal] + 1
  else:
    counter[lowercase_animal] = 1
print(counter)

# challenge for data structure
my_cohort = ['Kay', 'Kyrsten', 'Sapna', 'Cristina', 'Dave', 'Jonah']
name_count = {}
for each_item in my_cohort:
  first_letter = each_item[0]
  if first_letter in name_count:
    name_count[first_letter] = name_count[first_letter] + 1
  else:
    name_count[first_letter] = 1
print(name_count)
