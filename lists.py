names = ["Joe", "Jack", "Jane"]

#végigiterálunk a names változó elemein
for name in names:
    print(name)

#Enumerate függvényt kell hasznánli, ha az indexhez hozzá szeretnénk férni
for i, name in enumerate(names):
    print(i)
    print(name)

counter = 10
for name in names:
    print(counter)
    print(name)
    counter += 2  

# 1. írd ki az első három hónap nevét egymás alá!

months= ["Január" , "Február" , "Március"]
for month in months:
    print(month)

# 2. Írd ki, hogy "Az év egyik hónpja Január." az első három hónappal!

months= ["Január" , "Február" , "Március"]
for month in months:
    print(f"Az év egyik hónapja {month} .")


# 3. Hozz létre egy listát a 3, 7, 9, 13 számokkal! Add össze a 
# listában lévő számokat 

numbers = [3, 7, 9, 13]
sum = 0
for number in numbers:
    sum = sum + number
    print(sum)
    