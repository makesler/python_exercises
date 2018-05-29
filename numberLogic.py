# Don't delete any of the given code.
def numberFun(a, b, c):
  # insert your logic here
  if a + b == c:
    return True
  elif a - b == c or b - a == c:
    return True
  elif a * b == c:
    return True
  elif a / b == c or b / a == c:
    return True
  else:
    return False
  
  
# Test cases. Don't modify  
print(1,numberFun(1, 2, 3))	     # Possible
print(2,numberFun(4, 5, 1))	   	 # Possible
print(3,numberFun(10, 2, 4))	     # Impossible	
print(4,numberFun(9, 2, 18))	     # Possible
print(5,numberFun(9, 5, 14))	   	 # Possible
print(6,numberFun(90, 25, 65))	  # Possible 
print(7,numberFun(288, 16, 18))   # Possible
print(8,numberFun(56, 5, 260))    # Impossible
print(9,numberFun(4, 65, 260))    # Possible
