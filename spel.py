import random, time, os
global spelList

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

#           0           1          2         3        4         5                     6
spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma7(spelList):
    result = []
    for i in range (len(spelList)):
        result.append(random.choice(spelList))
    return result

def spelProgramma3(spelList):
    result = []
    for i in range (3):
        result.append(random.choice(spelList))
    return result

def spelProgramma10(spelList):
    result = []
    for i in range (10):
        result.append(random.choice(spelList))
    return result

print("3 spelen: ")
print(*spelProgramma3(spelList),sep='\n')
clearScreen(5)
print("7 spelen: ")
print(*spelProgramma7(spelList),sep='\n')
clearScreen(5)
print("10 spelen: ")
print(*spelProgramma10(spelList),sep='\n')
clearScreen(5)