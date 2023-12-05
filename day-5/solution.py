import sys
from typing import List


def clean_input(filepath: str) -> List[List[str]]:
    main_list = []
    with open(filepath) as f:
        section_list = []
        for line in f:
            line = line.strip()
            if line:
                section_list.append(line)
            else:
                main_list.append(section_list)
                section_list = []
        if section_list:
            main_list.append(section_list)
    return main_list


def part_one(input_list: List[List[str]]) -> int:
    seeds = [int(seed) for seed in input_list.pop(0)[0].split(': ')[1].split(' ')]
    min_loc = sys.maxsize
    mapping = []

    for m in input_list:
        m.pop(0)
        mapping.append([list(map(int, row.split(' '))) for row in m])

    for seed in seeds:
        current = seed 
        for mapp in mapping:
            for rangee in mapp:
                if current >= rangee[1] and current < rangee[1]+rangee[2]:
                    current = rangee[0] + current - rangee[1]
                    break
        min_loc = min(min_loc, current)

    return min_loc


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))