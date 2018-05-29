a = int(input())
b = int(input())

def love8(a, b):
  if a + b == 8 or b + a == 8 or a == 8 or b == 8 or a - b == 8 or b - a == 8:
    print("True")
  elif a + b != 8 or b + a != 8 or a != 8 or b != 8 or a - b != 8 or b - a != 8:
    print("False")
    
love8(a, b)
