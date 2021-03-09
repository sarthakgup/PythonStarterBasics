
'''import random
print(random.randrange(6), random.randrange(6))
print(random.randrange(1,7),random.randrange(1,7))
print(random.randrange(2,37,2))
print(random.randrange(1,36,2))'''


import math
def pizzaPrice(diameter):
    area = math.pi*(diameter/2)**2
    price = area * .15
    return price
size = int(input("What size(diameter) pizza do you want?"))
print("The price of yourpizza is $", roundund(pizzaPrice(size),2))

def smallestNumber(x,y,z):
    numbers = [x,y,z]
    print(min(numbers))

snallestNumber(5,10, 15).