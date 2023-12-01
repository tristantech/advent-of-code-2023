from typing import List

LOOKUP_INTS = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
}
LOOKUP_FULL = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def parse_line(line: str, allow_word_nums: bool) -> int:
    lookup = LOOKUP_FULL if allow_word_nums else LOOKUP_INTS

    def scan(reverse: bool) -> str:
        for i in range(len(line)):
            for token in lookup.keys():
                segment = line[len(line)-i-1:len(line)] if reverse else line[i:]
                if segment.startswith(token):
                    return lookup[token]

    return scan(reverse=False)*10 + scan(reverse=True)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    print("Part 1", sum((parse_line(l, False) for l in lines)))
    print("Part 2", sum((parse_line(l, True) for l in lines)))

if __name__ == "__main__":
    main()