if True:
    print("Ez mindig lefut")

if False:
    print("Ez sosem fut le")

if 5 > 10:
    print("Vajon lefut-e")

n = 10
n % 2 == 0 #Páros
n % 2 == 1 #Páratlan

# Kérj be a felhasználótól egy számot! Ha az páros, írd ki, hogy páros.
# Ha az páratlan, írd ki, hogy páratlan.

number = int(input("Adj meg egy számot!"))

if number % 2 == 0:
    print("Páros")

if number % 2 == 1:
    print("Páratlan")


#szam = int(input("Adj meg egy számot!"))
#maradek = szam % 2
#if maradek == 0:
#    print("Páros")
#if maradek == 1:
 #   print("Páratlan")