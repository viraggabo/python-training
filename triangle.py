base = int(input("Kérem az alapot"))
hight = int(input("Kérem a magasságot"))
area= base * hight / 2

print(f"A háromszög területe {area}") #f string a kapcsos zárólej mögötti részt kiértékeli


# az int függvény lebegőpontos számok esetén levágja a tizedesjegyeket
print(int(10))
print(int(10.0))
print(int(10.3))
print(int(10.5))
print(int(10.7))