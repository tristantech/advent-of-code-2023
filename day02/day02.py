from collections import Counter
from typing import List, Tuple

def parse_game(line:str) -> Tuple[int, List[dict]]:
    # Split at colon to separate game ID and draws
    game_str, draw_str = line.split(":", maxsplit=2)
    game_id = int(game_str[len("Game "):])

    draws = []
    for draw in draw_str.split(";"):
        draw_counts = Counter()
        for token in draw.split(","):
            count, color = token.strip().split(" ")
            draw_counts[color] += int(count)
        draws.append(draw_counts)

    return game_id, draws

def part1(lines: List[str]) -> int:
    return sum((
        game_id
        for game_id, draws in (
            parse_game(l) for l in lines
        )
        if all(((
                d.get("red", 0) <= 12 and
                d.get("green", 0) <= 13 and
                d.get("blue", 0) <= 14
            )
            for d in draws
        ))
    ))

def calculate_power(draws: List[dict]) -> int:
    return (
        max(draws, key=lambda x: x["red"])["red"] *
        max(draws, key=lambda x: x["green"])["green"] *
        max(draws, key=lambda x: x["blue"])["blue"]
    )

def part2(lines: List[str]) -> int:
    return sum((calculate_power(parse_game(l)[1]) for l in lines))

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    print("Part 1", part1(lines))
    print("Part 2", part2(lines))

if __name__ == "__main__":
    main()
