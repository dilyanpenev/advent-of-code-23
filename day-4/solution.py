from typing import List, Dict


def clean_input(filepath: str) -> Dict[int, str]:
    result_dict = dict()
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                card, nums = line.split(': ')
                card = int(card.split(' ')[-1])
                result_dict[card] = nums
    return result_dict


def part_one(input_dict: Dict[int, str]) -> int:
    ans = 0
    for _card, nums in input_dict.items():
        c = 1
        win, my = nums.split(' | ')
        winlist = [int(w) for w in win.split(' ') if w != '']
        mylist = [int(m) for m in my.split(' ') if m != '']
        for num in mylist:
            if num in winlist:
                c *= 2
        if c >= 1:
            ans += c//2
    return ans


def part_two(input_dict: Dict[int, str]) -> int:
    total_scratchcards = 0
    card_copies = [1]*(len(list(input_dict.keys())))
    for card, nums in input_dict.items():
        match = 0
        win, my = nums.split(' | ')
        winlist = [int(w) for w in win.split(' ') if w != '']
        mylist = [int(m) for m in my.split(' ') if m != '']
        for num in mylist:
            if num in winlist:
                match += 1
        for copy in range(card, card+match):
            if copy < len(card_copies):
                card_copies[copy] += card_copies[card-1]
        total_scratchcards += card_copies[card-1]

    return total_scratchcards


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    print("Solution for part 2 is {}".format(part_two(input_list)))
