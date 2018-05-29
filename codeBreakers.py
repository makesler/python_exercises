# the following will use python programs to help crack the codes. 
# Run the program to try and figure out the answers.

#import pycipher
import math

print('='*35)
print('Welcome to Python Cipher Hacker')
print('='*35)
print()
print('Which Cipher do you want to try?')
print('-'*35)
print('Enter 1 for Cesar Hacker')
print('Enter 2 for Vigenere Hacker')
print('Enter 3 for Keyword Ciper')
print('Enter 4 for Atbash Cipher')
print('Enter 5 for Columnar Transposition')
print('Enter 0 to Exit the program')
print('-'*35)
userInput = int(input('Enter your choice here: '))


def cesarHacker():
  print()
  print('Starting Cesar Hacker......')
  print()
  message = input('Enter the message to be decrypted: ')
  message = message.upper()
  LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  # loop through every possible key
  for key in range(len(LETTERS)):
  
      # It is important to set translated to the blank string so that the
      # previous iteration's value for translated is cleared.
      translated = ''
  
      # The rest of the program is the same as the original Caesar program:
  
      # run the encryption/decryption code on each symbol in the message
      for symbol in message:
          if symbol in LETTERS:
              num = LETTERS.find(symbol) # get the number of the symbol
              num = num - key
              # handle the wrap-around if num is 26 or larger or less than 0
              if num < 0:
                  num = num + len(LETTERS)
  
              # add number's symbol at the end of translated
              translated = translated + LETTERS[num]
  
          else:
              # just add the symbol without encrypting/decrypting
              translated = translated + symbol
  
      # display the current key being tested, along with its decryption
      translated = translated.lower()
      print('Key #%s: %s' % (key, translated))

      
def vigenereHacker():
    print()
    print('Vigenere Hacker.....')
    print('-'*30)
    key = input('Please enter the keyword: ').casefold()
    ciphertext = input('Enter the phrase to decrypt: ').casefold()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext
    
def keyword():
  print()
  print('Keyword Cipher.....')
  print('-'*30)
  message = input("Enter your message: ")
  key = input("What is the keyword? ")
  count = 0
  mode = "d"
  
  letters = "abcdefghijklmnopqrstuvwxyz" 
  translated_message = ""
  index = 0
  for character in message:
      if character in letters:
         number = letters.find(character)
         number = number - (ord(key[index]) - ord('a'))
         index = index+1
         index = index % len(key)
  
         if number >= len(letters):
              number = number - len(letters)
         elif number < 0:
              number = number + len(letters)
  
         translated_message = translated_message + letters[number]
      else:
           translated_message = translated_message + character
  
  print(translated_message)

def atbash():
  print()
  print('atbash program......')
  print('-'*30)
  message = input('Enter message to be decrypted: ')
  # every possible symbol that can be encrypted
  LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  # stores the encrypted/decrypted form of the message
  translated = ''
  # capitalize the string in message
  message = message.upper()
  # run the encryption/decryption code on each symbol in the message string
  for symbol in message:
      if symbol in LETTERS:
          # get the encrypted (or decrypted) number for this symbol
          num = LETTERS.find(symbol) # get the number of the symbol
          num = -num -1
          # add encrypted/decrypted number's symbol at the end of translated
          translated = translated + LETTERS[num]
      else:
          # just add the symbol without encrypting/decrypting
          translated = translated + symbol
  
  # print the encrypted/decrypted string to the screen
  print(translated)
  
def transposition():
    print()
    print('Transposition program......')
    print('-'*30)
    myMessage = input("Enter the encoded text: ")
    myKey = int(input("Enter the key: "))
    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext)


def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    col = 0   
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0            
            row += 1
    return ''.join(plaintext)


while True:
  if userInput == 1:
    cesarHacker()
  elif userInput == 2:
    print(vigenereHacker())
  elif userInput == 3:
    keyword()
  elif userInput == 4:
    atbash()
  elif userInput == 5:
    transposition()
  elif userInput == 0:
    break
  else:
    print('Please enter a valid number. Try again.')
    break
