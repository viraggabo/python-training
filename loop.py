# írjuk ki 5x egymás után a nevünket
#print("István\n" * 5)

# i, j, k
for i in range(5):
    print(i)
    print("Gábor")
print("End")

# Feladat: Írj egy ciklust, ami kiírja a számokat 1 től 100 ig egymás alá!

for i in range(100):
    i = i + 1
    print(i)


# Feladat: Írd ki egymás után a neved 5*, írd elé a sorszámot is!

for i in range(5):
    print(f" {i +1} Gábor")

# Feladat: Írj egy ciklust, amely 1 tól 10 ig kiírja
#  a számokat és azok négyzetét is új sorba

for i in range(10):
    j = i + 1
    result= j ** 2 # ** a négyzetet jelenti
    print(f"A {j} szám négyzete: {result} ")

# i felveszi a következő értéket: 5 <= i <10
for i in range(5, 10):
    print(i)

#harmadik paraméter a lépés
for i in range(10, 20, 2):
    print(i)

# lépés negatív szám , csökketni, esetünkben 10-től 1-ig
for i in range(10, 0, -1):
    print(i)
