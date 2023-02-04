"""
Coding Bootcamp at the Monroe Township Library

Class 9 Project

Dice Rolling Simulator
Create a simple dice rolling simulator that can handle any number of dice with any amount of sides
Simulator should allow users to reroll their dice as many times as they want
Should also give players a visual representation of their dice and a sum of dice values

-Dice that the user rolls will all be unique instances of the Dice class
-When new dice objects are created, we should simulate a roll automatically in the __init__ so they have a start value
-Rerolling a die should actually change its value, not just return a value
-Dice should be represented to the user in a clear way when printed
    -you can just use the die's value or some visual representation like |3| or (3)

-You will need to complete the methods in the Dice class, and other helper functions
"""


import random


class Dice:
    #complete these methods
    
    def __init__(self, sides):
        pass

    def __repr__(self):
        pass

    def reroll(self):
        pass


def display_dice(dice_list):
    """
    dice_list {list} -- list of the current dice objects created

    prints a visual display of rolled dice, as well as a sum of their values
    """

    #your code goes here!
    pass


def reroll_dice(dice_list):
    """
    dice_list {list} -- list of the current dice objects created

    returns {null} -- modifies the values of the dice in the current list
    """

    #your code goes here!
    pass


def main():
    """
    user interaction

    no need to modify anything in this function unless you want to!
    """

    print("Dice Rolling Simulator")
    print("----------")

    dice_list = []

    while True:
        amount = input("How many dice do you want to roll?: ")
        sides = input("How many sides should they have?: ")

        try:
            for i in range(int(amount)):
                new_dice = Dice(int(sides))
                dice_list.append(new_dice)

        except ValueError:
            print("Invalid input")
            print("----------")
            continue

        while True:
            display_dice(dice_list)

            reroll = input("Press Enter to reroll, or type 'q' to quit: ").lower()

            if reroll == "q":
                break
            else:
                reroll_dice(dice_list)

        break


if __name__ == "__main__":
    main()
