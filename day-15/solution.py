from typing import List
from collections import defaultdict


def clean_input(filepath: str) -> List[str]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                result_list = line.split(',')
    return result_list


def hash(s: str) -> int:
    value = 0
    for ch in s:
        value = ((value + ord(ch)) * 17) % 256
    return value


def part_one(steps: List[str]) -> int:
    ans = 0
    for step in steps:
        ans += hash(step)
    return ans


def part_two(steps: List[str]) -> int:
    boxes = defaultdict(list)
    for step in steps:
        if '=' in step:
            label, pw = step.split('=')
            v = hash(label)
            for el in boxes[v]:
                if el[0] == label:
                    el[1] = pw
                    break
            else:
                boxes[v].append([label, pw])
        else:
            label, _ = step.split('-')
            v = hash(label)
            for i, el in enumerate(boxes[v]):
                if el[0] == label:
                    boxes[v].pop(i)
                    break
    ans = 0
    for key, values in boxes.items():
        for idx, v in enumerate(values):
            ans += (key+1)*(idx+1)*int(v[1])
    return ans


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    print("Solution for part 2 is {}".format(part_two(input_list)))