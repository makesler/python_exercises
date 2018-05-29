# prints number of consonants in a string

word = input("In: ")
consonants = 'bcdfghjklmnpqrstvwxyz'
count = 0

for x in word:
  if x in consonants:
    count += 1
    
print(count)
