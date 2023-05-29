import numpy as np

suit = ['Diamond', 'Club', 'Heart', 'Spade']

suits = {'Diamond': "♦", 
         'Club': "♣",
         'Heart': "♥",
         'Spade': "♠"}

suitSymbols = list(suits.values())

cardNumber = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']



for suit in suitSymbols:
    for number in cardNumber:
        deck = [number, suit]


print(deck)


def drawPhase():
    draw = print("You drew ")

print("test12321321")