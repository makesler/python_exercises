# import anything necessary here.

# A1 - combining inputs * * * * * * * *
# This program reads two numbers and prints their sum:

"""
def sum_three():
  a = int(input())
  b = int(input())
  c = int(input())
  return (a+b+c)
  
print(sum_three())
"""

#A2 - Area of a Triangle * * * * * * * *

"""
def area_triangle():
  b = int(input())
  h = int(input())
  return (1/2*b*h)

print(area_triangle())
"""

#A3 - Combining Strings * * * * * * * *

"""
def name_input():
  name = input()
  return(name)

print('Hello,', name_input() + ".")
"""

#A4 - Find the larger of 2 numbers * * * * * * * *

"""
def print_bigger_number():
  integer1 = input()
  integer2 = input()
  
  if integer1 >= integer2:
    print("The bigger number is " + integer1)
  
  if integer2 >= integer1:
    print("The bigger number is " + integer2)

print_bigger_number()
"""

#A5 - Printing Arrays * * * * * * * *

"""
def print_food():
  food_items = ["turkey","ham", "spam","eggs","nuts"]

  print(food_items[3])
  print("This will print the array of food items")

  for x in food_items:
    print(x)

print_food()
"""

#A6 - Else if statements* * * * * * * *

"""
def find_grade():
  grade = int(input("Enter your grade: "))

  if grade > 89:
    print("A")
  elif grade > 79:
    print("B")
  elif grade > 69:
    print("C")
  elif grade > 59:
    print("D")
  elif grade > 49:
    print("F")
  elif grade < 50:
    print("F")
  
find_grade()
"""
  
#A7 - Partial Arrays * * * * * * * *

def print_less():
  a1 = [1, 1, 2, 3, 4, 5, 8, 11, 13, 17, 19, 20, 21, 34, 43, 55, 89]

  for x in a1:
    if (x < 30):
      print(x)

print_less()
