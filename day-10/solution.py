from typing import List, Tuple


def clean_input(filepath: str) -> List[List[str]]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                line = list(line)
                result_list.append(line)
    return result_list


def find_s(grid: List[List[str]]) -> List[int]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if 'S' == grid[row][col]:
                return [row, col]
            
    
def transform_path(pipe, current, prev):
    if pipe == '|':
        if current[0] - prev[0] == 1:
            return [current[0]+1, current[1]]
        else:
            return [current[0]-1, current[1]]
    elif pipe == '-':
        if current[1] - prev[1] == 1:
            return [current[0], current[1]+1]
        else:
            return [current[0], current[1]-1]
    elif pipe == 'L':
        if current[0] - prev[0] == 1:
            return [current[0], current[1]+1]
        else:
            return [current[0]-1, current[1]]
    elif pipe == 'F':
        if current[0] - prev[0] == -1:
            return [current[0], current[1]+1]
        else:
            return [current[0]+1, current[1]]
    elif pipe == 'J':
        if current[0] - prev[0] == 1:
            return [current[0], current[1]-1]
        else:
            return [current[0]-1, current[1]]
    elif pipe == '7':
        if current[0] - prev[0] == -1:
            return [current[0], current[1]-1]
        else:
            return [current[0]+1, current[1]]
    else:
        print('error')


def part_one(grid: List[List[str]]) -> int:
    s_pos = find_s(grid)
    print(s_pos)
    prev_left, prev_right = s_pos, s_pos
    left, right = [s_pos[0], s_pos[1]-1], [s_pos[0]+1, s_pos[1]]
    steps = 1
    while left != right:
        steps += 1
        nxt_left = transform_path(grid[left[0]][left[1]], left, prev_left)
        nxt_right = transform_path(grid[right[0]][right[1]], right, prev_right)
        prev_left, prev_right, left, right = left, right, nxt_left, nxt_right
    return steps


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    # print("Solution for part 2 is {}".format(part_two(input_list)))