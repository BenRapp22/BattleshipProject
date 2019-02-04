import numpy as np


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

#Displaying Game Board
a = np.arange(1, 11, 1)
list1 = [a]
array1 = np.array(list1, dtype = 'int')

for i in range(0,10):
    print(array1 + (10*i))

print("Use the following characters to select which type of ship you would like to place: ")
print("Aircraft Carrier -- AC")
print("Battleship -- B")
print("Cruiser -- C")
print("Destroyer -- D")
print("Submarine -- S")

#Placing Ships
x = 0
howmanyships = 0
shiplength = 0

while 1:
    while 1:
        whichship = input("Which ship would you like to place? ")
        if whichship == "AC":
            shiplength = 5
            howmanyships = howmanyships + 1
            break
        elif whichship == "B":
            shiplength = 4
            howmanyships = howmanyships + 1
            break
        elif whichship == "C":
            shiplength = 3
            howmanyships = howmanyships + 1
            break
        elif whichship == "D":
            shiplength == 2
            howmanyships = howmanyships + 1
            break
        elif whichship == "S":
            shiplength = 1
            howmanyships = howmanyships + 1
            break
        else:
            print("Try Again!")
    if howmanyships == 1:
        while 1:
            try:
                startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
                if 1 <= startinput <= 100:
                    break
                else:
                    print("Choose a space on the board!")
            except:
                print("Try Again!")
        Ship1 = [startinput, ]
        directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        if directioninput == "RIGHT":
            for i in range(1, int(shiplength)):
                Ship1.append(startinput + (i + x))
            break
        elif directioninput == "DOWN":
            for i in range(1, int(shiplength)):
                Ship1.append(startinput + ((10*i) + x))
            print(str(whichship) + ": " + str(Ship1))
            break
        else:
            print("Try Again!")
    elif howmanyships == 2:
        while 1:
            try:
                startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
                if 1 <= startinput <= 100:
                    break
                else:
                    print("Choose a space on the board!")
            except:
                print("Try Again!")
        Ship2 = [startinput, ]
        directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        if directioninput == "RIGHT":
            for i in range(1, int(shiplength)):
                Ship2.append(startinput + (i + x))
            break
        elif directioninput == "DOWN":
            for i in range(1, int(shiplength)):
                Ship2.append(startinput + ((10*i) + x))
            break
        else:
            print("Try Again!")
        print(str(whichship) + ": " + str(Ship2))
    elif howmanyships == 3:
        while 1:
            try:
                startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
                if 1 <= startinput <= 100:
                    break
                else:
                    print("Choose a space on the board!")
            except:
                print("Try Again!")
        Ship3 = [startinput, ]
        directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        if directioninput == "RIGHT":
            for i in range(1, int(shiplength)):
                Ship2.append(startinput + (i + x))
            break
        elif directioninput == "DOWN":
            for i in range(1, int(shiplength)):
                Ship3.append(startinput + ((10*i) + x))
            break
        else:
            print("Try Again!")
        print(str(whichship) + ": " + str(Ship3))
    elif howmanyships == 4:
        while 1:
            try:
                startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
                if 1 <= startinput <= 100:
                    break
                else:
                    print("Choose a space on the board!")
            except:
                print("Try Again!")
        Ship4 = [startinput, ]
        directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        if directioninput == "RIGHT":
            for i in range(1, int(shiplength)):
                Ship4.append(startinput + (i + x))
            break
        elif directioninput == "DOWN":
            for i in range(1, int(shiplength)):
                Ship4.append(startinput + ((10*i) + x))
            break
        else:
            print("Try Again!")
        print(str(whichship) + ": " + str(Ship4))
    elif howmanyships == 5:
        while 1:
            try:
                startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
                if 1 <= startinput <= 100:
                    break
                else:
                    print("Choose a space on the board!")
            except:
                print("Try Again!")
        Ship5 = [startinput, ]
        directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        if directioninput == "RIGHT":
            for i in range(1, int(shiplength)):
                Ship5.append(startinput + (i + x))
            break
        elif directioninput == "DOWN":
            for i in range(1, int(shiplength)):
                Ship5.append(startinput + ((10*i) + x))
            break
        else:
            print("Try Again!")
        print(str(whichship) + ": " + str(Ship5))
    elif howmanyships == 6:
        while 1:
            try:
                startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
                if 1 <= startinput <= 100:
                    break
                else:
                    print("Choose a space on the board!")
            except:
                print("Try Again!")
        Ship6 = [startinput, ]
        directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        if directioninput == "RIGHT":
            for i in range(1, int(shiplength)):
                Ship6.append(startinput + (i + x))
            break
        elif directioninput == "DOWN":
            for i in range(1, int(shiplength)):
                Ship6.append(startinput + ((10*i) + x))
            break
        else:
            print("Try Again!")
        print(str(whichship) + ": " + str(Ship6))
    elif howmanyships == 7:
        while 1:
            try:
                startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
                if 1 <= startinput <= 100:
                    break
                else:
                    print("Choose a space on the board!")
            except:
                print("Try Again!")
        Ship7 = [startinput, ]
        directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        if directioninput == "RIGHT":
            for i in range(1, int(shiplength)):
                Ship7.append(startinput + (i + x))
            break
        elif directioninput == "DOWN":
            for i in range(1, int(shiplength)):
                Ship7.append(startinput + ((10*i) + x))
            break
        else:
            print("Try Again!")
        print(str(whichship) + ": " + str(Ship7))
    else:
        break

    #while 1:
        #try:
            #startinput = int(input("Please Select Starting Space (keep in mind that ships are placed from left --> right and up --> down): "))
            #if 1 <= startinput <= 100:
                #break
            #else:
                #print("Choose a space on the board!")
        #except:
            #print("Try Again!")
    #Ship1 = [startinput, ]
    #while 1:
        #directioninput = input("Please Select Direction (type RIGHT to place from left --> right, and DOWN to place from up --> down): ")
        #if directioninput == "RIGHT":
            #for i in range(1, int(shiplength)):
                #Ship1.append(startinput + (i + x))
            #break
        #elif directioninput == "DOWN":
            #for i in range(1, int(shiplength)):
                #Ship1.append(startinput + ((10*i) + x))
            #break
        #else:
            #print("Try Again!")
    #print(str(whichship) + ": " + str(Ship1


#SHIPS CANT OVERLAP
#AC, B, and C CAN ONLY BE SELECTED ONCE
#FORCE USER TO MAKE PROPER INPUTS
