# checks if a password is valid

print('''Enter your new password:

Must contain:
1. At least eight characters long
2. Has lower case and upper case letters.
3. Has numbers and letters.
''')

input_primary = input('New Password:        ')
input_secondary = input('Enter password again:')

if len(input_primary) < 8:
  print("Password not long enough.")
else:
  print("Password is correct length.")

def hasNumbers(inputString):
  return any(char.isdigit() for char in inputString)
  
print(hasNumbers(input_primary))

def hasLetters(inputString):
  return any(char.isalpha() for char in inputString)
  
print(hasLetters(input_primary))
