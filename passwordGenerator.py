import random

char_count = int(input('How long do you want your password to be?'))

print("Enter [1] for letters")
print("Enter [2] for letters and numbers")
print("Enter [3] for numbers, letters & symbols")
password_type = int(input())

# Declare a list of characters for your password
if password_type == 1:
  characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

  for x in range (0, char_count):
    b = random.choice(characters)
    print(b, end="")
  

elif password_type == 2:
  characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

  for x in range (0, char_count):
    b = random.choice(characters)
    print(b, end="")

    
elif password_type == 3:
  characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "&"]

  for x in range (0, char_count):
    b = random.choice(characters)
    print(b, end="")
