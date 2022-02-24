value = True

if value:
  print("value is true")
else: 
  print("value is false")
print("This always Runs")

import random
random_number = random.randint(1, 5)
if random_number == 1:
   print("one") 
elif random_number == 2:
  print("Two")
else:
  print("Not one or two")

import time
seconds = int(time.time())
print({seconds})
if seconds % 3 == 0:
  print("Fizz")
elif seconds % 5 == 0:
  print("Buzz")
elif seconds % 5 == 0 & seconds % 3 == 0:
  print("FizzBuzz")
else:
  print({seconds})
