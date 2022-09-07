# A felhasználótól kérjetek be egy számot, és írjátok ki a kétszeresét
#egészen addig ismételjétek, amíg a felhasználó 0- át nem ír be.


#number = int(input("Adj meg egy számot!"))
#while number > 0:
 #   print(number * 2)

#DRY - don't repeat yourself

#number = int(input("Adj meg egy számot!"))
number = 100
while number!= 0:
    print(number * 2)
    number = int(input("Adj meg egy számot!"))