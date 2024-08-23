import random
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Step 1: Define the Card Class
class Card:
    def __init__(self, number, shape, color, shading):
        self.features = [number, shape, color, shading]
    
    def __repr__(self):
        return f"Card({self.features})"

# Step 2: Create the Deck
def create_deck():
    features = [1, 2, 3]
    deck = [Card(*features) for features in product(features, repeat=4)]
    return deck

# Step 3: Check if Three Cards Form a Set
def is_set(card1, card2, card3):
    for i in range(4):
        values = {card1.features[i], card2.features[i], card3.features[i]}
        if len(values) == 2:  # Values must be either all the same or all different
            return False
    return True

# Step 4: Find All Sets in a Given Hand
def find_sets(cards):
    sets = []
    for combo in combinations(cards, 3):
        if is_set(*combo):
            sets.append(combo)
    return sets

# Define shapes
def draw_shape(ax, shape, color, shading, x, y):
    if shape == 1:  # oval
        shape = patches.Ellipse((x, y), width=0.5, height=1, color=color, fill=(shading != 3))
    elif shape == 2:  # diamond
        shape = patches.Polygon([[x-0.25, y], [x, y+0.5], [x+0.25, y], [x, y-0.5]], color=color, fill=(shading != 3))
    elif shape == 3:  # squiggle (approximated as a sine wave)
        shape = patches.Polygon([[x-0.25, y+0.5], [x+0.25, y+0.5], [x+0.25, y-0.5], [x-0.25, y-0.5]], 
                                color=color, fill=(shading != 3))
    ax.add_patch(shape)
    
    # Add stripes for shading if necessary
    if shading == 2:
        for i in range(-5, 6):
            ax.plot([x-0.25, x+0.25], [y+i*0.1, y+i*0.1], color=color, linewidth=0.5)

# Define colors
def get_color(color):
    if color == 1:
        return "red"
    elif color == 2:
        return "green"
    elif color == 3:
        return "blue"

# Draw a card
def draw_card(card, position):
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-2, 2)
    ax.axis('off')
    
    number, shape, color, shading = card.features
    color = get_color(color)
    
    positions = [-1.5, 0, 1.5] if number == 3 else ([-0.75, 0.75] if number == 2 else [0])
    for i, pos in enumerate(positions):
        draw_shape(ax, shape, color, shading, 0, pos)
    
    plt.savefig(f"card_{position}.png", bbox_inches='tight')
    plt.show()

# Step 5: Example Game Play
from itertools import combinations

# Create and shuffle the deck
deck = create_deck()
random.shuffle(deck)

# Deal a hand of 12 cards
hand = deck[:12]
print("the value of hand is ", hand)
# Draw the hand
for i, card in enumerate(hand):
    draw_card(card, i)

# Find and print all sets in the hand
sets_in_hand = find_sets(hand)
print("\nSets found:")
for s in sets_in_hand:
    print(s)
