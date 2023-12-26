from typing import List, Dict, Tuple


def clean_input(filepath: str) -> Tuple[Dict[str, List[str]], List[Dict[str, int]]]:
    rules = dict()
    parts = []
    is_rule = True
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                if is_rule:
                    label, rule = line.replace('}', '').split('{')
                    rule = rule.split(',')
                    rules[label] = rule
                else:
                    elems = line.replace('{', '').replace('}', '').split(',')
                    part = dict()
                    for e in elems:
                        k, v = e.split('=')
                        part[k] = int(v)
                    parts.append(part)
            else:
                is_rule = False
    return rules, parts


def check_rule(rule: str, part: Dict[str, int]) -> bool:
    if '>' in rule:
        param, val = rule.split('>')
        return part.get(param) > int(val)
    elif '<' in rule:
        param, val = rule.split('<')
        return part.get(param) < int(val)
    else:
        return False


def part_one(rules: Dict[str, List[str]], parts: List[Dict[str, int]]) -> int:
    ans = 0
    for part in parts:
        state = 'in'
        while state != 'A' and state != 'R':
            for rule in rules.get(state):
                if ':' not in rule:
                    state = rule
                else:
                    r, v = rule.split(':')
                    if check_rule(r, part):
                        state = v
                        break
        if state == 'A':
            ans += sum(list(part.values()))
    return ans


def part_two(rules: Dict[str, List[str]]) -> int:
    pass

if __name__ == "__main__":
    rules, parts = clean_input('./input.txt')
    print("Solution for part 1 is {}".format(part_one(rules, parts)))
    print("Solution for part 2 is {}".format(part_two(rules)))