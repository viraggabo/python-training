# String egy adatszerkezet, hiszen karakterekből áll
name = "John Doe"
for c in name: # végigmegy a karaktereken
    print(c)

# Összeszámolja a névben lévő o betüket
count = 0
for c in name:
    if c == "o":
        count +=1
print(count)

print(name[3])

#Szeletelés, slicing
print(name[1:4])

print(len(name))

print("John" in "John Doe")
if "John" in name:
    print("Na, ez is egy újabb John")

#Stringeknek vannak saját függvényeik: metódusok

print(name.upper()) # a függvényt a name változó hívjuk meg
fruit = "   alma     "
print(fruit.strip())

print("john" in "Jack Jane John")
print("john" in "Jack Jane John".lower())
