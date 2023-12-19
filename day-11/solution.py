from typing import List


def clean_input(filepath: str) -> List[List[str]]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                result_list.append(list(line))
    return result_list


def transpose(i: List[List[str]]) -> List[List[str]]:
    return list(map(list, zip(*i)))


def expand_rows(i: List[List[str]]) -> List[List[str]]:
    expand = []
    empty = ['.']*len(i[0])
    for idx, row in enumerate(i):
        if all(c == '.' for c in row):
            expand.append(idx)
    for idx in expand[::-1]:
        i.insert(idx, empty)
    return i


def get_expanded_rows(i: List[List[str]]) -> List[str]:
    expand = []
    empty = ['.']*len(i[0])
    for idx, row in enumerate(i):
        if all(c == '.' for c in row):
            expand.append(idx)
    return expand


def part_one(starmap: List[List[str]]) -> int:
    # expand rows
    starmap = expand_rows(starmap)
    # expand columns
    starmap = transpose(expand_rows(transpose(starmap)))
    ans = 0
    galaxy = []
    for r, row in enumerate(starmap):
        for c, chr in enumerate(row):
            if chr == '#':
                for g in galaxy:
                    ans += abs(g[0]-r) + abs(g[1]-c)
                galaxy.append([r, c])
    return ans


def part_two(starmap: List[List[str]]) -> int:
    expanded_rows = get_expanded_rows(starmap)
    expanded_cols = get_expanded_rows(transpose(starmap))
    ans = 0
    galaxy = []
    for r, row in enumerate(starmap):
        for c, chr in enumerate(row):
            if chr == '#':
                for g in galaxy:
                    ans += abs(g[0]-r) + abs(g[1]-c)
                    for exp in expanded_cols:
                        if (exp > g[1] and exp < c) or (exp < g[1] and exp > c):
                            ans = ans - 1 + 1000000
                galaxy.append([r, c])
    return ans


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    print("Solution for part 2 is {}".format(part_two(input_list)))