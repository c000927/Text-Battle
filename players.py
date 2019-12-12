# Charlie Sun
# CS 30
# Period 4
# December 3, 2019
# Player File of the game

# Import libraries
import random
import cmd
import sys
import os
import time
import textwrap


class Player:
    """Player class that allows to generate a player"""
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

    def playerAttack(self, enemy):
        """Attack function for players"""
        print("You are attacking the enemy.")
        accuracyNum = random.randrange(0, 10) / 10
        if accuracyNum <= self.accuracy:
            enemy.hp = enemy.hp - self.ap
            print("The enemy HP now is: " + str(enemy.hp))
        else:
            print("You missed the shot!")
