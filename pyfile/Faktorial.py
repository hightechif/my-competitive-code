total = 1
n = raw_input()
if n == 0:
  total = total  
else:
  for i in range(int(n)):
    total = total * (i+1)
 
print total
length = len(str(total))
print '\n', length
