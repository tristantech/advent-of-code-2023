from collections import Counter
from typing import List, Tuple

def parse_card(line: str) -> Tuple[int, int]:
    _, numbers = line.strip().split(": ")
    parts = numbers.split(" | ")

    return len(
        {int(x) for x in parts[0].split(" ") if x.isdigit()} &
        {int(x) for x in parts[1].split(" ") if x.isdigit()}
    )

def part1(match_counts: List[int]) -> int:
    return sum((
        (2**(x-1) if x else 0) for x in match_counts
    ))

def part2(match_counts: List[int]) -> int:
    card_quantities = Counter()

    for i in range(len(match_counts)):
        # Count the original card
        card_quantities[i] += 1
        for j in range(match_counts[i]):
            # Update quantities of N cards ahead
            card_quantities[i+1+j] += card_quantities[i]

    return card_quantities.total()

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    match_counts = [
        match_count
        for match_count in map(parse_card, lines)
    ]

    print("Part 1", part1(match_counts))
    print("Part 2", part2(match_counts))

if __name__ == "__main__":
    main()
