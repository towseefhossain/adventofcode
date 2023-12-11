from enum import Enum
from functools import cmp_to_key

class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def compare(set_a, set_b):
    hand_a = set_a[0]
    hand_b = set_b[0]
    if (hand_a[1].value < hand_b[1].value):
        return -1
    elif (hand_a[1].value > hand_b[1].value):
        return 1
    else:
        for i in range(0, 5):
            if cards[hand_a[0][i]] < cards[hand_b[0][i]]:
                return -1
            elif cards[hand_a[0][i]] > cards[hand_b[0][i]]:
                return 1
    return 0

def calculate_type_of_hand(hand: str) -> HandType:
    hand_dict = {}
    for card in hand:
        if (hand_dict.get(card)):
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1
    
    values = list(hand_dict.values())
    if 5 in values:
        return HandType.FIVE_OF_A_KIND
    elif 4 in values:
        return HandType.FOUR_OF_A_KIND
    elif 3 in values: 
        if 2 in values:
            return HandType.FULL_HOUSE
        else:
            return HandType.THREE_OF_A_KIND
    elif 2 in values:
        if values.count(2) == 2:
            return HandType.TWO_PAIR
        else:
            return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD

def solve():
    res = {}
    with open('day7.txt') as file:
        for line in file:
            elements = line.strip().split()
            res[(elements[0], calculate_type_of_hand(elements[0]))] = int(elements[1])
    result = sorted(list(res.items()), key=cmp_to_key(compare))
    total = 0
    for idx, item in enumerate(result):
        total += ((idx + 1) * (item[1])) 
    print(total)

if __name__ == "__main__":
    solve()