import random

print("================================")
print("Welcome to Rock, Paper, Scissors")
print("================================")
print()

choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

player = False
userwins = 0
compwins = 0

while player == False:
  #sets player to True
  player = input('Rock, Paper, or Scissors?: \n')
  
  if player == computer:
    print("Tie!")
  elif player == "Rock":
    if computer == "Scissors":
      print("You win! Rock smashes scissors!")
      userwins += 1
    else: 
      print('You lose! Paper covers rock!')
  elif player == "Scissors":
    if computer == "Paper":
      print("You win! Scissors cut paper!")
      userwins += 1
    else: 
      print('You lose! Rock smashes scissors!')
  elif player == "Paper":
    if computer == "Rock":
      print("You win! Paper covers rock!")
      compwins += 1
    else: 
      print('You lose! Scissors cut paper!')
      compwins += 1
  else:
    print("> That's not a valid input. Check spelling.")
  print('=========================')
  print('\nScore: ')
  print('Computer Score: ', compwins)
  print('Player Score: ', userwins)
  print('=========================')
  print()
  player = False
  computer = random.choice(choices)
