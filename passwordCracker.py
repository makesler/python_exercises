import string
import itertools

def guess_password(real):
  chars = string.ascii_lowercase + string.digits      #all letters and numbers
  attempts = 0
  
  for password_length in range (1, 6):      #length of password
    for guess in itertools.product(chars, repeat = password_length):
      attempts += 1      #adds an attempt each loop
      guess = ''.join(guess)
      if guess == real:
        return  'password is {}, it was found in {} guesses'.format(guess, attempts)
      #print(guess, attempts)

print(guess_password('beach'))
