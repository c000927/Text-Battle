# Charlie Sun
# CS 30
# Period 4
# December 3, 2019
# Main File of the game

# Import libraries
import random
import cmd
import sys
import os
import time
import textwrap


# Player class that allows to generate a player
class Player:
    def __init__(self, list, hp, ap, accuracy, weapons):
        self.name = ""
        self.hp = hp
        self.ap = ap
        self.accuracy = accuracy
        self.weapons = weapons
        self.alive = True
        self.oldLocation = "."
        self.newLocation = "."
        self.locationX = 0
        self.locationY = 0
        self.activeAxisY = list[0]
        self.tempAxisY = list[0]

    # Attack function for players
    def playerAttack(self, enemy):
        print("You are attacking the enemy.")
        accuracyNum = random.randrange(0, 10) / 10
        if accuracyNum <= self.accuracy:
            enemy.hp = enemy.hp - self.ap
            print("The enemy HP now is: " + str(enemy.hp))
        else:
            print("You missed the shot!")


# Enemy class that allows to generate a enemy
class Enemy():
    def __init__(self):
        self.hp = 0
        self.ap = 0
        self.accuracy = 0
        self.alive = True

    # Attack function for enemy
    def enemyAttack(self, player):
        print("Enemy is attacking " + player.name + ".")
        accuracyNum = random.randrange(0, 10) / 10
        if accuracyNum <= self.accuracy:
            player.hp = player.hp - self.ap
            print("Your HP now is: " + str(player.hp))
        else:
            print("Enemy missed the shot!")


class Monster(Enemy):
    def __init__(self):
        self.hp = 0
        self.ap = 0
        self.accuracy = 0
        self.alive = True

# The function that generate the enemies
def enemyGenerator(level, ap, hp, accuracy):
    cEnemy = Enemy()
    cEnemy.ap = ap
    cEnemy.hp = hp
    cEnemy.accuracy = accuracy
    cEnemy.alive is True
    return cEnemy

def monsterGenerator(level, ap, hp, accuracy):
    cMonster = Monster()
    cMonster.ap = ap
    cMonster.hp = hp
    cMonster.accuracy = accuracy
    cMonster.alive is True
    return cMonster

# Initial map configuration
initMap = """
X1....
.1....
.1....
.1...W
"""

# Create a new map
newMap = initMap.split()

# Convert the initial map into a nested list
mapNestedList = []
for lines in initMap.split():
    mapNestedList.append(list(lines))


# The move funciton
def move():
    global newMap

    # Convert the map into a nested list
    mapNestedList = []
    for lines in newMap:
        mapNestedList.append(list(lines))

    # Calculate the maximum y axis number
    maxAxisY = len(mapNestedList) - 1

    # Initialize user input
    userInput = ""

    # Function that locates the player
    def locationFinder():
        # Reset search indicator
        searchIndicator = 0
        # Reset found indicator
        foundIndicator = False
        # If player location is found and search indicator is smaller than max
        while foundIndicator is False and searchIndicator <= maxAxisY:
            try:
                dPlayer.locationX = mapNestedList[searchIndicator].index("X")
                dPlayer.locationY = searchIndicator
                foundIndicator = True
            except:
                # Add 1 to search indicator
                searchIndicator = searchIndicator + 1

    # Function that display the map
    def worldDisplay(maxAxisY):
        indicator = 0
        # while the interval is smaller than the accepted value:
        while indicator <= maxAxisY:
            print(*mapNestedList[indicator], sep="")
            indicator = indicator + 1

    # Function that find the event
    def eventFinder(eventCode):
        global currentEnemy

        def baseFunc():
            if "w" in userInput or "s" in userInput:
                dPlayer.tempAxisY.insert(dPlayer.locationX, "X")
                del dPlayer.activeAxisY[dPlayer.locationX]
            dPlayer.activeAxisY.insert(dPlayer.locationX, dPlayer.oldLocation)

        if eventCode == ".":
            baseFunc()

        if eventCode == "1":
            baseFunc()
            currentEnemy = enemyGenerator(1, 10, 100, 0.1)

        if eventCode == "W":
            baseFunc()
            print("You won the game!")

    # Function that updates the map
    def mapUpdater(maxAxisY):
        global newMap
        lineList = []
        indicator = 0
        # while the interval is smaller than the accepted value:
        while indicator <= maxAxisY:
            lineList.append(mapNestedList[indicator])
            newMap = list(lineList)
            indicator = indicator + 1

    # Main move function
    while userInput != "quit":
        userInput = input(">> ").lower()
        locationFinder()
        dPlayer.activeAxisY = mapNestedList[dPlayer.locationY]
        if userInput == "attack":
            print("Attack successful")
        # Move west
        elif userInput == "a":
            if dPlayer.locationX != 0:
                dPlayer.oldLocation = dPlayer.newLocation
                dPlayer.newLocation = dPlayer.activeAxisY.pop(dPlayer.
                                                              locationX - 1)
                eventFinder(dPlayer.newLocation)
                mapUpdater(maxAxisY)
                print("You moved west!")
                break
            else:
                print("You can't move that way!")
        # Move east
        elif userInput == "d":
            if dPlayer.locationX != len(dPlayer.activeAxisY) - 1:
                dPlayer.oldLocation = dPlayer.newLocation
                dPlayer.newLocation = dPlayer.activeAxisY.pop(dPlayer.
                                                              locationX + 1)
                eventFinder(dPlayer.newLocation)
                mapUpdater(maxAxisY)
                print("You moved east!")
                break
            else:
                print("You can't move that way!")
        # Move north
        elif userInput == "w":
            if dPlayer.activeAxisY != mapNestedList[0]:
                try:
                    dPlayer.tempAxisY = mapNestedList[dPlayer.locationY - 1]
                    dPlayer.oldLocation = dPlayer.newLocation
                    dPlayer.newLocation = dPlayer.tempAxisY.pop(dPlayer.
                                                                locationX)
                    eventFinder(dPlayer.newLocation)
                    mapUpdater(maxAxisY)
                    print("You moved north!")
                    break
                except:
                    print("You can't move that way!")
            else:
                print("You can't move that way!")
        # Move south
        elif userInput == "s":
            if dPlayer.activeAxisY != mapNestedList[maxAxisY]:
                try:
                    dPlayer.tempAxisY = mapNestedList[dPlayer.locationY + 1]
                    dPlayer.oldLocation = dPlayer.newLocation
                    dPlayer.newLocation = dPlayer.tempAxisY.pop(dPlayer.
                                                                locationX)
                    eventFinder(dPlayer.newLocation)
                    mapUpdater(maxAxisY)
                    print("You moved south!")
                    break
                except:
                    print("You can't move that way!")
            else:
                print("You can't move that way!")
        # Quit the game
        elif userInput == "quit":
            print("Quiting the game")
        # Error handling
        else:
            print("Invalid input")


# The function that print out the title screen menu
def titleScreen():
    # Clear the UI of terminal
    # os.system("clear")
    # Print the menu out
    print("- - - - - - - - - - - - - - - - -")
    print("- - - Welcome to TextBattle - - -")
    print("- - - - - - - - - - - - - - - - -")
    print("-            # Play #           -")
    print("-            # Help #           -")
    print("-            # Quit #           -")
    print("-  Copyright 2019 Charlie Sun   -")
    print("- - - - - - - - - - - - - - - - -")
    # Call the user input function
    titleScreenSelection()


# The function that print out the help menu
def gameHelp():
    # Print the help out
    print("- - - - - - - - - - - - - - - - -")
    print("- - - - - - Help Menu - - - - - -")
    print("- - - - - - - - - - - - - - - - -")
    print("-      Type #PLAY# to play      -")
    print("-           Then #GO#           -")
    print("-        Move: TYPE #GO#        -")
    print("-        East: TYPE #D#         -")
    print("-        West: TYPE #A#         -")
    print("-        North: TYPE #W#        -")
    print("-        South: TYPE #S#        -")
    print("- - - - - - - - - - - - - - - - -")
    # Call the user input function
    titleScreenSelection()


# The function that let user select items by input
def titleScreenSelection():
    # Get the user selection
    selection = input(">> ").lower()
    # Redirect to play function if user selected play
    if selection == "play":
        gamePlayInit()
    # Redirect to help function if user selected help
    elif selection == "help":
        gameHelp()
    # Quit the game if user selected quit
    elif selection == "quit":
        sys.exit()
    # Error handling if user input something else
    while selection.lower() not in ["play", "help", "quit"]:
        print("Invalid command.")
        selection = input(">> ").lower()
        if selection == "play":
            gamePlayInit()
        elif selection == "help":
            gameHelp()
        elif selection == "quit":
            sys.exit()


# The function that loop the main game play
def gamePlayInit():
    global dPlayer
    # os.system("clear")
    # Ask the player for their role
    question1 = "So, what role do you want to use?\n"
    question1_1 = "Choose from Assault, CQB, Demolition, Supporter and Sniper."
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in question1_1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    playerRole = input(">> ")
    roles = ["assault", "cqb", "demolition", "supporter", "sniper"]
    if playerRole.lower() in roles:
        print("You choosed " + playerRole + " as your role.\n")
        # Setup the player role
        if playerRole == "Assault":
            dPlayer = Player(mapNestedList, 100, 90, 0.8, ["M4A1", "M9"])
        elif playerRole == "CQB":
            dPlayer = Player(mapNestedList, 110, 30, 0.7, ["HK MP5", "HK45CT"])
        elif playerRole == "Demolition":
            dPlayer = Player(mapNestedList, 110, 80, 0.55, ["M870", "P226"])
        elif playerRole == "Supporter":
            dPlayer = Player(mapNestedList, 70, 70, 0.65,
                             ["M249 SAW", "Glock 17"])
        elif playerRole == "Sniper":
            dPlayer = Player(mapNestedList, 40, 100, 0.85,
                             ["MK 20 Mod 0 SSR", "M9"])
    while playerRole.lower() not in roles:
        print("You role is invalid.\n")
        playerRole = input(">> ")
        if playerRole.lower() in roles:
            print("You choosed " + playerRole + " as your role.\n")
            # Setup the player role
            if playerRole == "Assault":
                dPlayer = Player(mapNestedList, 100, 90, 0.8, ["M4A1", "M9"])
            elif playerRole == "CQB":
                dPlayer = Player(mapNestedList, 110, 30, 0.7,
                                 ["HK MP5", "HK45CT"])
            elif playerRole == "Demolition":
                dPlayer = Player(mapNestedList, 110, 80, 0.55,
                                 ["M870", "P226"])
            elif playerRole == "Supporter":
                dPlayer = Player(mapNestedList, 70, 70, 0.65,
                                 ["M249 SAW", "Glock 17"])
            elif playerRole == "Sniper":
                dPlayer = Player(mapNestedList, 40, 100, 0.85,
                                 ["MK 20 Mod 0 SSR", "M9"])

    # Ask the player for their name
    question2 = "Hi, what's your name?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    playerName = input(">> ")
    dPlayer.name = playerName

    gameLoop()


# The main game loop
def gameLoop():
    global dPlayer
    global currentEnemy
    counter = 0
    while dPlayer.alive is True:
        if counter == 0:
            print("Please choose where you want to go first:")
            move()
            counter += 1
        elif counter % 2 == 0 and counter != 0:
            print("Please type your action:")
            userInput = input(">> ").lower()
            if userInput == "go":
                move()
                counter += 1
            elif userInput == "attack":
                dPlayer.playerAttack(currentEnemy)
                counter += 1
            while userInput not in ["go", "attack", "w", "s", "a", "d"]:
                print("Invalid input!")
                print("Please type your action:")
                userInput = input(">> ").lower()
                if userInput == "go":
                    move()
                    counter += 1
                elif userInput == "attack":
                    dPlayer.playerAttack(currentEnemy)
                    counter += 1
        elif counter % 2 == 1:
            try:
                if currentEnemy.hp > 0:
                    currentEnemy.enemyAttack(dPlayer)
                    counter += 1
                else:
                    print("Enemy is dead.")
                    counter += 1
            except:
                print("Enemy takes no action this round!")
                counter += 1
        else:
            print("Round error!")
            counter += 1


# Call the title screen function
titleScreen()
