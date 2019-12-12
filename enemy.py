# Charlie Sun
# CS 30
# Period 4
# December 3, 2019
# Enemy File of the game

# Import libraries
import random
import cmd
import sys
import os
import time
import textwrap


class Enemy():
    """Enemy class that allows to generate a enemy"""
    def __init__(self):
        self.hp = 0
        self.ap = 0
        self.accuracy = 0
        self.alive = True

    def enemyAttack(self, player):
        """Attack function for enemy"""
        print("Enemy is attacking " + player.name + ".")
        accuracyNum = random.randrange(0, 10) / 10
        if accuracyNum <= self.accuracy:
            player.hp = player.hp - self.ap
            print("Your HP now is: " + str(player.hp))
        else:
            print("Enemy missed the shot!")


class Monster(Enemy):
    """Enemy class that allows to generate a monster"""
    def __init__(self):
        self.hp = 0
        self.ap = 0
        self.accuracy = 0
        self.alive = True
