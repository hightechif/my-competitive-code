import random

def cost(b):
    return (b - 4)**2

def num_slope(b):
    h = 0.0001
    return (cost(b+h) - cost(b))/h

def slope(b):
    return 2 * (b - 4)

b = random.random()

# Training loop
for i in range(10000):
    b = b - .1 * slope(b)
print(b)
