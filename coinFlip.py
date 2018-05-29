import random

num = int(input('How many times do you want to flip a coin?\n'))

heads_score = 0
tails_score = 0

choices = ["heads", "tails"]

for x in range (0, num):
  r_choice = random.choice(choices)
  
  if (r_choice == "heads"):
    heads_score += 1
  elif (r_choice == "tails"):
    tails_score += 1
  
print("\nTotal Coin Flips")
print("==================")
print('Heads: ', heads_score)
print('Tails: ', tails_score)
