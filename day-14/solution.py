from typing import List


def clean_input(filepath: str) -> List[List[str]]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                line = list(line)
                result_list.append(line)
    return result_list


def part_one(mapping: List[List[str]]) -> int:
    ans = 0
    rows, cols = len(mapping), len(mapping[0])
    for i in range(cols):
        border, padding = rows, 0
        for j in range(rows):
            if mapping[j][i] == '#':
                border, padding = rows-j, 1
            elif mapping[j][i] == 'O':
                ans += border - padding
                padding += 1
    return ans


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    # print("Solution for part 2 is {}".format(part_two(input_list)))