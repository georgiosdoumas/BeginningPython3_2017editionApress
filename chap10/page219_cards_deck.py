#!/usr/local/bin/python3
from random import shuffle

values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v, s) for v in values for s in suits]
shuffle(deck)

print("We start from a full deck of cards, and give you 1 card as long as you press ENTER")
print("If you want to stop before the ", len(deck), " cards of the deck are presented, type q and then Enter")
n = 0
while deck:
    c = input(deck.pop())
    n += 1
    if c == 'q':
        print("You decided to quit, after ", n, " cards were presented to you.")
        break
else:
    print("All cards were presented to you! Exiting")
