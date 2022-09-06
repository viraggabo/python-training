# input függvény
# paraméter: mit kell kiírni
#visszatérési értéke: a felhasználó által beírt érték
#Bekérjük a felhasználó nevét
name = input("Mi a neved?")
print(name)

#Kiírás : Helló [megadott név]!
#Trainer esetén Helló Trainer!

print("Helló " + name + "!")

# Kérjétek be a felhasználó életkorát!
#Írjátok ki aa kétszeresét!

age = int(input("Hány éves vagy?"))
print(type(age))
print(age  * 2)

"10" # String literál
10 # int literál

print("10" * 2)
print(10 * 2)
# konverziós függvény
print(type(int("10")))