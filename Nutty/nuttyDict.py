import time, os

from random import randint
from string import capwords

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

mmColors = {
    'Oranje': 0,
    'Blauw' : 0,
    'Groen' : 0,
    'Bruin' : 0,
    }

def createNeg():
    global mmColorsNeg,mmColorsList
    mmColorsNeg = {}
    mmColorsList = list(mmColors)
    for i in range(len(mmColorsList)):
        mmColorsNeg.update({i:mmColorsList[i]})

def mmBagFill(amount):
    for i in range(amount):
        mmColors[mmColorsNeg[randint(0,len(mmColorsList)-1)]] += 1

def main():
    createNeg()
    ask = int(input("Hoeveel M&M's? "))
    if isinstance(ask,int) and ask > 0:
        mmBagFill(ask)
        for x,y in mmColors.items(): 
            if y > 0:
                print(f'{y:>2}x {capwords(x)}')
        clearScreen(10)
        main()
    elif type(ask) != int:
        print('Niet een nummer, probeer opnieuw')
        main()
    elif ask < 1:
        print('Negatief getal, probeer opnieuw')
        main()

main()