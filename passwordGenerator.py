import random
import string


chars = string.ascii_letters + string.digits 
# string.punctuation
print(chars)

randombool=True
while randombool:
  try:
    number= int(input('Number of passwords?-'))

    length= int(input('Password length: '))

    randombool=False

  except:
    print("Please enter a valid input")

for p in range(number):
  password=''
  for c in range(length):
    password+= random.choice(chars)
  print(password)


