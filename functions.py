# def greet(name):
#   return f'Hello, {name}!'
# print(greet("Kyrsten"))
# # Prints: "Hello, Kyrsten!"
# print(greet("Kay Lack"))
# # Prints: "Hello, Kay Lack!"

def add_five(num):
  return 5 + num
print(add_five(4))
# Should print: "9"
print(add_five(2132))
# Should print: "2137"

def subtract_low_from_high(num1, num2): # Your code goes here.
  if num1 > num2:
    return num1 - num2
  else:
    return num2 - num1
print(subtract_low_from_high(2, 3))
# Should print "1"

print(subtract_low_from_high(3, 2))
# Should print "1"

print(add_five(subtract_low_from_high(1463, 16475)))
# Should print "15017"

def superify(item):
  return f"Super{item}"
print(superify("Frog"),(superify(superify(superify("Frog")))))
# Should print:
# "superfrog supersupersuperfrog"
print(superify("Frog")+(superify(superify(superify("Frog")))))
# Should print:
# "superfrogsupersupersuperfrog"