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
    current = [(65, 65)]
    next = set()
    for _ in range(64):
        for point in current:
            x, y = point[0], point[1]
            if mapping[x+1][y] != '#':
                next.add((x+1, y))
            if mapping[x-1][y] != '#':
                next.add((x-1, y))
            if mapping[x][y+1] != '#':
                next.add((x, y+1))
            if mapping[x][y-1] != '#':
                next.add((x, y-1))
        current = list(next)
        next = set()
    return len(current)


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    # print("Solution for part 2 is {}".format(part_two(input_list)))