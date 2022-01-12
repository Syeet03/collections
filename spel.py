import random
global spelList

#           0           1          2         3        4         5                     6
spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList):
    result = []
    for i in range (len(spelList)):
        result.append(random.choice(spelList))
    return result

print(spelProgramma(spelList))