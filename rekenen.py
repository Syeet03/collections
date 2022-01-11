#Imports
import time,os

#Maakt scherm leeg
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def addAndDisplayList(listOne, listTwo):
    result = []
    for i in range(len(listOne)):
        result.append(listOne[i] + listTwo[i])
    return result

for i in range(len(listOne)):
    print(listOne[i], "+", listTwo[i], "=", addAndDisplayList(listOne, listTwo)[i])

clearScreen(10)


def subtractAndDisplayList(listOne, listTwo):
    result = []
    for i in range(len(listOne)):
        result.append(listOne[i] - listTwo[i])
    return result

for i in range(len(listOne)):
    print(listOne[i], "-", listTwo[i], "=", subtractAndDisplayList(listOne, listTwo)[i])

clearScreen(10)


def multiplyAndDisplayList(listOne, listTwo):
    result = []
    for i in range(len(listOne)):
        result.append(listOne[i] * listTwo[i])
    return result

for i in range (len(listOne)):
    print(listOne[i], "*", listTwo[i], "=", multiplyAndDisplayList(listOne, listTwo)[i])

clearScreen(10)


def divideAndDisplayList(listOne, listTwo):
    result = []
    for i in range(len(listOne)):
        result.append(listOne[i] / listTwo[i])
    return result

for i in range (len(listOne)):
    print(listOne[i], "/", listTwo[i], "=", divideAndDisplayList(listOne, listTwo)[i])

clearScreen(10)