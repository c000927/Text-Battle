# Charlie Sun
# CS 30
# Period 4
# November 8, 2019
# The main game loop that allow continuous game play

# Import libraries
import random
import cmd
import sys
import os
import time
import textwrap


def title_screen():
    """The function that print out the title screen menu"""
    # Clear the UI of terminal
    os.system("clear")
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
    title_screen_selection()


def game_help():
    """The function that print out the help menu"""
    # Print the help out
    print("- - - - - - - - - - - - - - - - -")
    print("- - - - - - Help Menu - - - - - -")
    print("- - - - - - - - - - - - - - - - -")
    print("-      Type #PLAY# to play      -")
    print("-     Then #GO# or #ATTACK#     -")
    print("-        Move: TYPE #GO#        -")
    print("-        East: TYPE #D#         -")
    print("-        West: TYPE #A#         -")
    print("-        North: TYPE #W#        -")
    print("-        South: TYPE #S#        -")
    print("-        Attack: TYPE #ATTACK#  -")
    print("- - - - - - - - - - - - - - - - -")
    # Call the user input function
    title_screen_selection()


def title_screen_selection():
    """The function that let user select items by input"""
    # Get the user selection
    selection = input(">> ")
    # Redirect to play function if user selected play
    if selection.lower() == "play":
        game_play()
    # Redirect to help function if user selected help
    elif selection.lower() == "help":
        game_help()
    # Quit the game if user selected quit
    elif selection.lower() == "quit":
        sys.exit()
    # Error handling if user input something else
    while selection.lower() not in ["play", "help", "quit"]:
        print("Invalid command.")
        selection = input(">> ")
        if selection.lower() == "play":
            game_play()
        elif selection.lower() == "help":
            game_help()
        elif selection.lower() == "quit":
            sys.exit()


def game_play():
    """The function that loop the main game play"""
    print("Please type your action:")
    # Get the user selection
    selection = input(">> ")
    # Ask where user want to go if user selected go
    if selection.lower() == "go":
        print("Where do you want to go?")
        direction = input(">> ")
        # Go north if user selected North
        if direction.lower() == "w":
            print("You are going north.")
            game_play()
        # Go south if user selected s
        elif direction.lower() == "s":
            print("You are going south.")
            game_play()
        # Go west if user selected a
        elif direction.lower() == "a":
            print("You are going west.")
            game_play()
        # Go east if user selected d
        elif direction.lower() == "d":
            print("You are going east.")
            game_play()
        # Error handling if user input something else
        while direction.lower() not in ["w", "s", "a", "d"]:
            print("Invalid input. Please try again.")
            direction = input(">> ")
            if direction.lower() == "w":
                print("You are going north.")
                game_play()
            elif direction.lower() == "s":
                print("You are going south.")
                game_play()
            elif direction.lower() == "a":
                print("You are going west.")
                game_play()
            elif direction.lower() == "d":
                print("You are going east.")
                game_play()
    # Let user attack if user selected attack
    elif selection.lower() == "attack":
        print("You are attacking!")
        game_play()
    # Quit the game if user selected to quit
    elif selection.lower() == "quit":
        sys.exit()
    # Error handling if user selected something else
    while selection.lower() not in ["go", "attack", "quit"]:
        print("Invalid input, please try again!")
        game_play()
