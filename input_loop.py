# Kérj be egy egész számot és írd ki addig az összes egész páros számot!
#pl 8, akkor legyen kiírva 2, 4, 6, 8

number = int(input("Kérek egy számot!"))
print(number)
for i in range(2, number +1, 2):

    print(i)

