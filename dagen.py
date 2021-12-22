#Imports
import time,os

#Maakt scherm leeg
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

#        0           1         2            3            4          5           6         
dagen = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']

print('Alle dagen: ')
for dag in dagen:
    print(dag)
clearScreen(10)

print('Werkdagen: ')
for werkdag in dagen[:-2]:
    print(werkdag)
clearScreen(10)

print('Weekenddagen: ')
print(dagen[-2])
print(dagen[-1])
clearScreen(10)

print('Alle dagen in omgekeerde volgorde: ')
for dag in reversed(dagen):
    print(dag)
clearScreen(10)

print('Werkdagen in omgekeerde volgorde: ')
for werkdag in reversed(dagen[:-2]):
    print(werkdag)
clearScreen(10)

print('Weekenddagen in omgekeerde volgorde: ')
print(dagen[-1])
print(dagen[-2])
clearScreen(10)