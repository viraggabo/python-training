fruits = ["apple", "raspberry", "cherry"]
print(fruits.index("raspberry"))

for fruit in fruits:
    print(fruit)

print(len(fruits))

print(fruits[1])

print(fruits[1:3])

print("apple" in fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

#Óriási különbség: a lista módosítható:
fruits = ["apple", "raspberry", "cherry"]
fruits [1] = "banana"
print(fruits)

fruits.append("peach")
print(fruits)