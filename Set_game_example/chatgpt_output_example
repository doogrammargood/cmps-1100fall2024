class Card:
    def __init__(self, number, shape, color, shading):
        self.features = [number, shape, color, shading]
    
    def __repr__(self):
        return f"Card({self.features})"
from itertools import product

def create_deck():
    features = [1, 2, 3]
    deck = [Card(*features) for features in product(features, repeat=4)]
    return deck
def is_set(card1, card2, card3):
    for i in range(4):
        values = {card1.features[i], card2.features[i], card3.features[i]}
        if len(values) == 2:
            return False
    return True
from itertools import combinations

def find_sets(cards):
    sets = []
    for combo in combinations(cards, 3):
        if is_set(*combo):
            sets.append(combo)
    return sets
import random

# Create and shuffle the deck
deck = create_deck()
random.shuffle(deck)

# Deal a hand of 12 cards
hand = deck[:12]

# Print the hand
print("Hand:")
for card in hand:
    print(card)

# Find and print all sets in the hand
sets_in_hand = find_sets(hand)
print("\nSets found:")
for s in sets_in_hand:
    print(s)
