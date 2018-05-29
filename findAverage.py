# input how many arrays
num_arrays = int(input("How many arrays do you want to find the average of?"))

#Hint:
output = []
for i in range (0, num_arrays):
  a = input().split()
  a = [int(x) for x in a]

  calc = sum(a) / len(a)
  output.append(calc)
print(output)
