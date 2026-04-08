# Assignemnt 2 - Card Draw
# Author - Michal Gondek

import requests

# Shuffle a new deck of cards
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
data = response.json()

deck_id = data['deck_id']

# Draw 5 cards from the deck
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
cards_data = response.json()

cards = cards_data['cards']

# Print the drawn cards
print('Your Cards Are:\n')

values = []
suits = []  

for card in cards:
    value = card['value']
    suit = card['suit']
    values.append(value)
    suits.append(suit)
    print(f"{value} of {suit}")

# Check for straight, pairs, three of a kind, and four of a kind
value_map = {
    'ACE': 14, 'KING': 13, 'QUEEN': 12, 'JACK': 11,
    '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}

numeric_values = sorted([value_map[v] for v in values])

from collections import Counter
value_counts = Counter(values)

is_pair = 2 in value_counts.values()
is_triple = 3 in value_counts.values()
is_flush = len(set(suits)) == 1

is_straight = all(numeric_values[i] + 1 == numeric_values[i + 1] for i in range(4))

if numeric_values == [2, 3, 4, 5, 14]: 
    is_straight = True

print('\nResult:')

if is_flush:
    print("Flush")
elif is_straight:
    print("Straight")
elif is_triple:
    print("Three of a Kind")      
elif is_pair:
    print("Pair")
else:
    print('No special hand.')
