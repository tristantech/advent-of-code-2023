import re

from typing import List

lookup = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def parse_line(line: str, allow_word_nums: bool) -> int:
    tokens = []
    for i in range(len(line)):
        if line[i].isdigit():
            tokens.append(line[i])
            continue
        if not allow_word_nums:
            continue
        for t in lookup.keys():
            if line[i:].startswith(t):
                tokens.append(t)
                break

    def convert(t):
        if t.isdigit():
            return int(t)
        return lookup[t]

    return convert(tokens[0]) * 10 + convert(tokens[-1])

def part1(lines: List[str]):
    return sum((parse_line(l, False) for l in lines))

def part2(lines: List[str]):
    return sum((parse_line(l, True) for l in lines))

def main():
    words = []
    with open("input.txt", "r") as f:
        words = f.readlines()

    print("Part 1", part1(words))
    print("Part 2", part2(words))

if __name__ == "__main__":
    main()