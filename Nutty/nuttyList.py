import time, os

from random import randint
from string import ascii_lowercase,capwords

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

mmColors = ["Oranje", "Blauw", "Groen", "Bruin"]

def intConvert(num):
    numConvert1 = False
    numConvert2 = True

    alphabet = list(ascii_lowercase)

    for i in range(10):
        if str(i) in num:
            numConvert1 = True

    for x in range(26):
        if alphabet[x] in num:
            numConvert2 = False
    
    if numConvert1 and numConvert2:
        return int(num)
    else:
        return num

def mmBagFill(amount):
    mmBagList = []
    for i in range(amount):
        mmBagList.append(mmColors[randint(0,len(mmColors)-1)])
    for i in range(len(mmBagList)):
        mmBagList[i] = capwords(mmBagList[i])
    return mmBagList

def sortbag(list):
    list.sort()
    return list

def main():
    ask = intConvert(input("Hoeveel M&M's? "))
    if isinstance(ask, int) and ask > 0:
        print(*sortbag(mmBagFill(ask)),sep=', ')
        clearScreen(10)
        main()
    elif type(ask) != int:
        print("Niet een nummer, probeer opnieuw.")
        main()
    elif ask <1:
        print("Negatief getal, probeer opnieuw.")
    elif ask > len(mmColors):
        print("Te veel kleuren, probeer opnieuw.")

main()