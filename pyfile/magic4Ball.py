import random

def getAnswer(n):
  if n == 1:
    return 'It is certain'
  elif n == 2:
    return 'It is decidedly so'
  elif n == 3:
    return 'Yes'
  elif n == 4:
    return 'Reply hazy try again'
  elif n == 5:
    return 'Congratulations!'

r = random.randint(1, 5)
fortune = getAnswer(r)
print(fortune)
