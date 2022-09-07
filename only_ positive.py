numbers= [23, 54, 0, 76, -10, 0, 54, -21, -35, 10, 0]
sum = 0
for number in numbers:
    
    if number > 0:
        sum = sum + number
print(sum)

#Számoljuk meg, és írjuk ki, hogy a listában hány nulla szerepel!
numbers= [23, 54, 0, 76, -10, 0, 54, -21, -35, 10, 0]
count = 0
for n in numbers:
    
    if n == 0:
        count = count + 1
print(count)