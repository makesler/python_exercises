#check how to read and open a file from A20
message_file = open('alice.txt','r')
message_file = [word for word in message_file]
#create a function to count a specified word

userInput = str((input("Enter what you want to find:")))
def countWord(file_object, word):
  count = 0
  for line in file_object:
    if word in line:
      count += 1
  return count
  
total = countWord(message_file, userInput)
print("The word '"+userInput+"' appears "+str(total) +" times")
