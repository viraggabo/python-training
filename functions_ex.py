# Írjátok meg a signum függvényt
#Ha a szám kiseeb mint 0 akkor -1-et ad vissza
#ha 0, akkor 0 át ad vissza
# ha nagyobb, mint 0 akkor 1-et ad vissza

def signum(number):




    if number<0:
        return -1
    elif number == 0:
        return 0
    else:
         return 1

print(signum(30))


#Írjatok egy függvényt, ami vár egy egész számot és visszaadja
#annak abszolútértékét

def abszolut(n):
    if n < 0:
        return n * -1
    else:
        return n

print (abszolut(-10))

#Írjatok egy függvényt, 
# amely várja a téglalap a és b oldalát, és vissza adja a területét

def terulet(a ,b):
    return a * b
print((terulet(5 ,10)))



#Írjatok egy függvényt, 
# amely várja a téglalap a és b oldalát, és vissza adja a kerületét

def calculate_perimeter(a ,b):
    return 2 * (a + b)
print((calculate_perimeter(3 ,6)))

#Írjatok egy függvényt, amely vár két számot, és visszaadja a
#kettő közül a nagyobbat!

def number(a ,b):
    if a > b:
        return a
    else:
        return b
    
print (number(20, 2))

#Vár egy számot és visszaadja a "páros" szöveget, ha páros,
#ellenkező esetben "páratlan"

def get_type(n):
    if n % 2 ==0:
        return "páros"
    else:
        return "páratlan"
print (get_type(4))

# Ha a függvény boolean értéket ad vissza, akkor
#logikai függvény: True vagy False


#Írj egy is_even nevű függvényt, mely a paraméterről
#eldönti, hogy páros-e!
#True-t adjon vissza, ha páros, False érétket adjon vissza,
#ha páratlan

def is_even(n):
    if n %2 == 0:
        return True
    else:
        return False
print(is_even(4))

