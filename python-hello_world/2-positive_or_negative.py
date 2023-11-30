#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("The number is", number)
print("if the number is greater than 0: is positive" if number > 0 
      else "if the number is 0: is zero" if number == 0 
      else "if the number is less than 0: is negative")