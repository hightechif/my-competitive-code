total = 1
n = int(input())
if n == 0:
  total = total  
else:
  for i in range(int(n)):
    total = total * (i+1)
 
length = len(str(total))
print(total, length)
