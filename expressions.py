print(5) # paramétere literál
age = 25
print(age) # paraméter változó

1 + 1 # kifejezés
# Operátor - körülötte az operandusok
print(1 + 1) # függvénynek paraméterül át lehet adni kifejezést is
print(1 + 1 + 1) # Függvények paraméterül át lehet adni kifejezést is

print(2 - 1)
print(15 / 5 )
print( 6 * 8)

print(3 + 4 * 2)
#precedencia szerint a szorzás erősebb, mint az összeadás
print((3 + 4) * 2) # Zárójelekkel a precedencia felülírható

print(5 ** 3) # Hatványozás

print(16 / 5)
print(16 // 5) # Egész osztás
print(16 % 5)  #M aradék

favourit_number = 6
print(favourit_number * 2)

a = 6
b = 10
print(a * b)

#Legyen egy változó, melynek nemve year_of_birth, születési éve,
# értéke legyen 1970
#Legyen egy változó, a year ami tartalmazza a jelenlegi év 2022
# Az age változóban tároljátok el, hogy az ember hány éves

year_of_birth = 1970
year = 2022
age = year - year_of_birth
print(age)

counter = 1
print (counter)

counter +=2 # counter = counter + 2
print(counter)

counter +=2 
print(counter)

# 15 = counter + 2 # Ez hibás, nem lehet literálnak értéket adni

# Operátorok működése stringeken

print("hello" + "world")
print(5 * "abc")
print(8 * "a")
#print("abc" - "bcd") # HIBÁS, kivonás nem értelmezett