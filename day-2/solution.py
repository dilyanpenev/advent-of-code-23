from typing import List, Dict


def clean_input(filepath: str) -> Dict[str, List[str]]:
    input_dict = dict()
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                game, sets = line.split(": ")
                game = game.split(' ')[1]
                sets = sets.replace(';', ',').split(', ')
                input_dict[game] = sets
    return input_dict


def part_one(input_dict: Dict[str, List[str]]) -> int:
    ans = 0
    maximum = {'red': 12, 'green': 13, 'blue': 14}
    for game, sets in input_dict.items():
        for set in sets:
            value, colour = set.split(' ')
            if int(value) > maximum.get(colour):
                break
        else:
            ans += int(game)
    return ans

def part_two(input_dict: Dict[str, List[str]]) -> int:
    ans = 0
    for _game, sets in input_dict.items():
        minimum = {'red': 0, 'green': 0, 'blue': 0}
        for set in sets:
            value, colour = set.split(' ')
            if int(value) > minimum.get(colour):
                minimum[colour] = int(value)
        power = minimum['blue'] * minimum['green'] * minimum['red']
        ans += power
    return ans


if __name__ == "__main__":
    input_dict = clean_input('./input.txt')
    print("Answer to Part 1 is {}".format(part_one(input_dict)))
    print("Answer to Part 2 is {}".format(part_two(input_dict)))
