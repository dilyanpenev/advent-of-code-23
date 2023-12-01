from typing import List


def clean_input(filepath: str) -> List[str]:
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                result_list.append(line)
    return result_list


def part_one(calibs: List[str]) -> int:
    ans = []
    for val in calibs:
        left, right = 0, len(val) - 1
        ischange = True
        while ischange and left < right:
            ischange = False
            if not val[left].isdigit():
                ischange = True
                left += 1
            if not val[right].isdigit():
                ischange = True
                right -= 1
        ans.append(int("{}{}".format(val[left], val[right])))
    return sum(ans)


def part_two(calibs: List[str]) -> int:
    ans = 0
    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    for val in calibs:
        left, right = 0, 0
        idx, n = 0, len(val)
        while idx < n:
            if val[idx].isdigit():
                left = int(val[idx])
                break
            if idx >= 2 and val[idx-2:idx+1] in ["one", "two", "six"]:
                left = nums.get(val[idx-2:idx+1])
                break
            if idx >= 3 and val[idx-3:idx+1] in ["four", "five", "nine"]:
                left = nums.get(val[idx-3:idx+1])
                break
            if idx >= 4 and val[idx-4:idx+1] in ["three", "seven", "eight"]:
                left = nums.get(val[idx-4:idx+1])
                break
            idx += 1

        idx = n - 1
        while idx >= 0:
            if val[idx].isdigit():
                right = int(val[idx])
                break
            if idx <= n-3 and val[idx:idx+3] in ["one", "two", "six"]:
                right = nums.get(val[idx:idx+3])
                break
            if idx <= n-4 and val[idx:idx+4] in ["four", "five", "nine"]:
                right = nums.get(val[idx:idx+4])
                break
            if idx <= n-5 and val[idx:idx+5] in ["three", "seven", "eight"]:
                right = nums.get(val[idx:idx+5])
                break
            idx -= 1

        ans += left*10 + right
    return ans
    

if __name__ == "__main__":
    input_list = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(input_list)))
    print("Solution for part 2 is {}".format(part_two(input_list)))