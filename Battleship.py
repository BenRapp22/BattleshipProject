import numpy as np

#Horizontal Grid
ah = np.arange(1, 11, 1)
bh = np.arange(11, 21, 1)
ch = np.arange(21, 31, 1)
dh = np.arange(31, 41, 1)
eh = np.arange(41, 51, 1)
fh = np.arange(51, 61, 1)
gh = np.arange(61, 71, 1)
hh = np.arange(71, 81, 1)
ih = np.arange(81, 91, 1)
jh = np.arange(91, 101, 1)

z = np.array([[ah], [bh], [ch], [dh], [eh], [fh], [gh], [hh], [ih], [jh]])

def boardmodel():
    print(z)

horizontalgrid = [ah, bh, ch, dh, eh, fh, gh, hh, ih, jh]
#Introduction
print("Welcome to Battleship! This is a 1-player game, in which the objective is to sink your opponent's battleships!")
print("Please place your own ships according to the diagram below, and only place your ships horizontally or vertically")
print("You have a total of 7 ships! You have: ")
print("1x Aircraft Carrier (5 Spaces Long)")
print("1x Battleship (4 Spaces Long)")
print("1x Cruiser (3 Spaces Long)")
print("2x Destroyer (2 Spaces Long)")
print("2x Submarine (1 Space Long)")
print("When entering your ")
print("Choose your positions wisely!")
boardmodel()

#User Places Ships
carrier1 = input("Aircraft Carrier Space 1: ")
carrier2 = input("Aircraft Carrier Space 2: ")
carrier3 = input("Aircraft Carrier Space 3: ")
carrier4 = input("Aircraft Carrier Space 4: ")
carrier5 = input("Aircraft Carrier Space 5: ")

battleship1 = input("Battleship Space 1: ")
battleship2 = input("Battleship Space 2: ")
battleship3 = input("Battleship Space 3: ")
battleship4 = input("Battleship Space 4: ")

cruiser1 = input("Cruiser Space 1: ")
cruiser2 = input("Cruiser Space 2: ")
cruiser3 = input("Cruiser Space 3: ")

destroyerA1 = input("Destroyer A Space 1: ")
destroyerA2 = input("Destroyer B Space 2: ")

destroyerB1 = input("Destroyer B Space 1: ")
destroyerB2 = input("Destroyer B Space 2: ")

submarineA = input("Submarine A Position: ")
submarineB = input("Submarine B Position: ")

if carrier2 == (carrier1 + 1):




#Another array with vertical orietnation
#User inputs specific numbers to indicate location of Ships
#Stores as a variable, tests against array(s)
#Computer attacks with a random number
