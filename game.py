from colorama import init
init()
from colorama import Fore

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
    'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
    'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

# Game Setup
player1 = Player("One")
player2 = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(Fore.CYAN + f"\nRound {round_num}")

    if len(player1.all_cards) == 0:
        print(Fore.YELLOW + 'Player 1 is out of cards! Player 2 wins!')
        break

    if len(player2.all_cards) == 0:
        print(Fore.YELLOW + 'Player 2 is out of cards! Player 1 wins!')
        break

    player1_cards = [player1.remove_one()]
    player2_cards = [player2.remove_one()]

    at_war = True

    while at_war:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            at_war = False

        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            at_war = False

        else:
            print(Fore.RED + "WAR!")

            if len(player1.all_cards) < 3:
                print(Fore.CYAN + "Player 1 unable to declare war.")
                print(Fore.GREEN + "Player 2 Wins!")
                game_on = False
                break

            elif len(player2.all_cards) < 3:
                print(Fore.CYAN + "Player 2 unable to declare war.")
                print(Fore.GREEN + "Player 1 Wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())

print(Fore.MAGENTA + f"\nGame over after {round_num} rounds.")
