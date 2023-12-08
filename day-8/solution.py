import re
import math
from typing import List, Dict, Tuple


def get_instructions(filepath: str) -> str:
    with open(filepath) as f:
        return f.readline().strip()


def clean_graph(filepath: str) -> Dict[str, Tuple[str, str]]:
    graph = dict()
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if re.search("\w{3} = \(\w{3}, \w{3}\)", line):
                locs = re.findall("\w{3}", line)
                graph[locs[0]] = (locs[1], locs[2])
    return graph


def part_one(instructions: str, graph: Dict[str, Tuple[str, str]]) -> int:
    ans = 0
    inst_idx = 0
    current = 'AAA'
    while current != 'ZZZ':
        if instructions[inst_idx] == 'L':
            current = graph.get(current)[0]
        else:
            current = graph.get(current)[1]
        inst_idx += 1
        ans += 1
        if inst_idx >= len(instructions):
            inst_idx = 0
    return ans


def part_two(instructions: str, graph: Dict[str, Tuple[str, str]]) -> int:
    inst_idx = 0
    current = [node for node in graph.keys() if re.match("\w{2}A", node)]
    periods = [0] * len(current)

    # Make everything end in Z
    for idx in range(len(current)):
        while not re.match("\w{2}Z", current[idx]):
            if instructions[inst_idx] == 'L':
                current[idx] = graph.get(current[idx])[0]
            else:
                current[idx] = graph.get(current[idx])[1]
            periods[idx] += 1
            inst_idx += 1
            if inst_idx >= len(instructions):
                inst_idx = 0

    # Calculate least common multiple
    lcm = 1
    for p in periods:
        lcm = lcm*p//math.gcd(lcm, p)
    return lcm


if __name__ == "__main__":
    instructions = get_instructions('./input.txt')
    loc_graph = clean_graph('./input.txt')
    print("Solution for part 1 is {}".format(part_one(instructions, loc_graph)))
    print("Solution for part 2 is {}".format(part_two(instructions, loc_graph)))