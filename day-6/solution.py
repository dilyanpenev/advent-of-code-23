from typing import List


def clean_input(filepath: str) -> List[List[int]]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                values = line.split(':')[1].strip()
                current_line = [int(v) for v in values.split(' ') if v != '']
                result_list.append(current_line)
    return result_list


def part_one(input_data: List[List[int]]) -> int:
    time, distance = input_data[0], input_data[1]
    ans = 1
    for idx in range(len(time)):
        cnt = 0
        for acc in range(time[idx]):
            if acc * (time[idx] - acc) > distance[idx]:
                cnt += 1
        ans *= cnt
    return ans


def part_two(input_data: List[List[int]]) -> int:
    time, distance = int(''.join(map(str, input_data[0]))), int(''.join(map(str, input_data[1])))
    ans = 0
    for t in range(time+1):
        if t * (time - t) > distance:
            ans += 1
    return ans


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    print("Solution for part 2 is {}".format(part_two(input_list)))