# Hozzatok éltre egy a változót, melynek értéke legyen 5
# Hozzatok éltre egy b változót, melynek értéke legyen 6

#Írjátok ki a következőt, de csak a változóknak a felhasználásával
# Az 5 + 6 kifejezés értéke: 11

a = 5 # int
b = 6 #int
result =a + b

print("Az "+ str(a) + " + " + str(b) +" kifejezés értéke: " + str(result))

print("Az", a, "+", b, "Kifejezés értéke:", result) #6 paraméteres hívás
#Paramétereket egymás után space-szel elválasztav írja ki

#String interpolation, formázott string, f-string
print(f" Az {a} + {b} kifejezés értéke: {a + b}")

print(5 + 5)
#print(5 + "5") #HIBA
print("5" + "5")# 55
