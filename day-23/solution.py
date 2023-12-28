from typing import List, Tuple
import sys


def clean_input(filepath: str) -> List[List[str]]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                line = list(line)
                result_list.append(line)
    return result_list


def part_one(maze: List[List[str]]) -> int:
    rows, cols = len(maze), len(maze[0])
    start, end = (0, 1), (140, 139)

    max_path = -1
    stack = [[start]]
    while stack:
        paths = stack.pop(-1)
        current = paths[-1]
        if current == end:
            max_path = max(max_path, len(paths)-1)

        if current[0]+1 < rows and maze[current[0]+1][current[1]] not in ['#', '^'] and (current[0]+1, current[1]) not in paths:
            stack.append(paths+[(current[0]+1, current[1])])
        if current[0]-1 >= 0 and maze[current[0]-1][current[1]] not in ['#', 'v'] and (current[0]-1, current[1]) not in paths:
            stack.append(paths+[(current[0]-1, current[1])])
        if current[1]+1 < cols and maze[current[0]][current[1]+1] not in ['#', '<'] and (current[0], current[1]+1) not in paths:
            stack.append(paths+[(current[0], current[1]+1)])
        if current[1]-1 >= 0 and maze[current[0]][current[1]-1] not in ['#', '>'] and (current[0], current[1]-1) not in paths:
            stack.append(paths+[(current[0], current[1]-1)])
    
    return max_path


def part_two(maze: List[List[str]]) -> int:
    rows, cols = len(maze), len(maze[0])
    start, end = (0, 1), (140, 139)

    max_path = -1
    stack = [[start]]
    while stack:
        paths = stack.pop(-1)
        current = paths[-1]
        if current == end:
            max_path = max(max_path, len(paths)-1)

        if current[0]+1 < rows and maze[current[0]+1][current[1]] != '#' and (current[0]+1, current[1]) not in paths:
            stack.append(paths+[(current[0]+1, current[1])])
        if current[0]-1 >= 0 and maze[current[0]-1][current[1]] != '#' and (current[0]-1, current[1]) not in paths:
            stack.append(paths+[(current[0]-1, current[1])])
        if current[1]+1 < cols and maze[current[0]][current[1]+1] != '#' and (current[0], current[1]+1) not in paths:
            stack.append(paths+[(current[0], current[1]+1)])
        if current[1]-1 >= 0 and maze[current[0]][current[1]-1] != '#' and (current[0], current[1]-1) not in paths:
            stack.append(paths+[(current[0], current[1]-1)])
    
    return max_path


if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    print("Solution for part 2 is {}".format(part_two(input_list)))