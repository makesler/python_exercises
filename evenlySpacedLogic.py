# Check if given numbers are evenly spaced

def evenlySpaced(small, big, goal):
  # insert your logic here
  list = [small, big, goal]
  sort_list = sorted(list)

  if sort_list[2] - sort_list[1] == sort_list[1] - sort_list[0]:
    return True
  else:
    return False

# Test cases. Don't modify  
print(1,evenlySpaced(2, 4, 6))   # this would be True
print(2,evenlySpaced(4, 6, 2))   # this would be True
print(3,evenlySpaced(4, 6, 3))   # this would be False
print(4,evenlySpaced(6, 2, 4))
print(5,evenlySpaced(6, 2, 8))
print(6,evenlySpaced(2, 2, 2))
print(7,evenlySpaced(2, 2, 3))
print(8,evenlySpaced(9, 10, 11))
print(9,evenlySpaced(10, 9, 11))
print(10,evenlySpaced(10, 9, 9))
print(11,evenlySpaced(2, 4, 4))
print(12,evenlySpaced(2, 2, 4))
print(13,evenlySpaced(3, 6, 12))
print(14,evenlySpaced(12, 3, 36))
