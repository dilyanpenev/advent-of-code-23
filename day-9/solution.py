from typing import List, Optional


def clean_input(filepath: str) -> List[List[int]]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                nums = [int(num) for num in line.split(' ')]
                result_list.append(nums)
    return result_list


def solve_helper(nums: List[int]) -> Optional[int]:
    diffs = [nums[idx]-nums[idx-1] for idx in range(1, len(nums))]
    if all(c == 0 for c in diffs):
        return 0
    else:
        return solve_helper(diffs) + diffs[-1]

def solve(num_lists: List[List[int]], part_two=False) -> int:
    ans = 0
    for nums in num_lists:
        if part_two:
            nums = list(reversed(nums))
        diff = solve_helper(nums)
        nxt = nums[-1] + diff
        ans += nxt

    return ans


if __name__ == "__main__":
    input_lists = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(solve(input_lists)))
    print("Solution for part 2 is {}".format(solve(input_lists, True)))