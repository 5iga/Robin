import random

numbers = list()



i = 0

while i<5:
    num = random.randint(100,200)
    if num%2 == 0:
        numbers.append(num)
        i = i + 1
        
print(numbers)