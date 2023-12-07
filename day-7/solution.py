from typing import List, Dict
from collections import defaultdict, Counter


def clean_input(filepath: str) -> Dict[str, int]:
    hands = dict()
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                cards, bid = line.split(' ')
                hands[cards] = int(bid)
    return hands


def get_hand_type(cards: str) -> int:
    freq = Counter(list(cards)).most_common()
    # Five of a kind
    if freq[0][1] == 5:
        return 7
    # Four of a kind
    elif freq[0][1] == 4:
        return 6
    elif freq[0][1] == 3:
        # Full house
        if freq[1][1] == 2:
            return 5
        # Three of a kind
        else:
            return 4
    elif freq[0][1] == 2:
        # Two pair
        if freq[1][1] == 2:
            return 3
        # One pair
        else:
            return 2
    # High card
    else:
        return 1


def part_one(hands: Dict[str, int]) -> int:
    ans = 0
    cards = list(hands.keys())
    types_dict = defaultdict(list)
    for card in cards:
        t = get_hand_type(card)
        types_dict[t].append(card)

    card_order = "AKQJT98765432"
    rank = len(cards)
    for _type, cards in sorted(types_dict.items(), reverse=True):
        for hand in sorted(cards, key=lambda card: [card_order.index(c) for c in card]):
            ans += hands[hand] * rank
            rank -= 1
    return ans


def get_hand_type_with_jokers(cards: str) -> int:
    cnt = Counter(list(cards))
    jacks = cnt['J']
    freq = [f for f in cnt.most_common() if f[0] != 'J']
    n = len(freq)

    # All Js
    if freq == []:
        return 7

    # Five of a kind
    elif freq[0][1] == 5:
        return 7

    # Four of a kind
    elif freq[0][1] == 4:
        if jacks == 1:
            return 7
        else:
            return 6

    elif freq[0][1] == 3:
        # Full house
        if n == 2:
            if freq[1][1] == 2:
                return 5
            else:
                return 6
        elif n == 1:
            return 7
        # Three of a kind
        else:
            return 4

    elif freq[0][1] == 2:
        if n == 1:
            return 7
        elif n == 2:
            if freq[1][1] == 2:
                return 5
            else:
                return 6
        elif n == 3:
            if freq[1][1] == 2:
                return 3
            else:
                return 4
        # Two pair
        else:
            return 2

    # High card
    else:
        if jacks == 4:
            return 7
        elif jacks == 3:
            return 6
        elif jacks == 2:
            return 4
        elif jacks == 1:
            return 2
        else:
            return 1


def part_two(hands: Dict[str, int]) -> int:
    ans = 0
    cards = list(hands.keys())
    types_dict = defaultdict(list)
    for card in cards:
        t = get_hand_type_with_jokers(card)
        types_dict[t].append(card)

    card_order = "AKQT98765432J"
    rank = len(cards)
    for _type, cards in sorted(types_dict.items(), reverse=True):
        for hand in sorted(cards, key=lambda card: [card_order.index(c) for c in card]):
            ans += hands[hand] * rank
            rank -= 1
    return ans


if __name__ == "__main__":
    hands = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(hands)))
    print("Solution for part 2 is {}".format(part_two(hands)))