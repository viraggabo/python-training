# Kérjétek be, hogy a felhasználó mikor született!
#import datetime
#Írjátok ki, hogy ezek alapján hány éves!
#De ne csak egy számot, hanem a következő üzenetet:

# Mivel xxxx-ben születtél, ezért yy éves vagy
#1. Kérjük be hogy mikor született! - int-é kell konvertálni
#2. Számoljuk ki, hogy hány éves egy age változóba (2022 - ből ki kell vonni)
#3. Írjuk ki  f-stringel a megadott üzenetet

#from datetime import datetime

date= int(input("mikor születtél?"))
age= 2022-date

print(f" Mivel {date}-ben születtél ezért {age} éves vagy.")

#actual_year= datatime.now().year