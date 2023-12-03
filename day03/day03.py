from collections import defaultdict
from typing import List, Tuple

class Parser:
    def __init__(self, lines: List[str]) -> None:
        self.grid = [l.strip() for l in lines]
        self.adj_sym_map = defaultdict(lambda: [])

        # Parsing state vars
        current_num = None
        adjacent_sym_found = False
        adjacent_sym_info = None

        # Search for numbers and store them along with info about their
        # adjacent symbol. (Discard numbers that don't have an adj. sym.)
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if not char.isdigit():
                    # Update state at the end of a number or end of a line
                    if current_num is not None and adjacent_sym_found:
                        # Have a number that is adjacent to a symbol
                        self.adj_sym_map[adjacent_sym_info].append(current_num)
                    current_num = None
                    adjacent_sym_found = False
                    adjacent_sym_info = None
                    continue

                # Add digit to (or start) current number.
                current_num = (10 * current_num if current_num is not None else 0) + int(char)
                
                has, sym_info = self._adjacent_symbol(x, y)
                if has:
                    # Found an adjacent symbol. Keep track of it.
                    adjacent_sym_found = True
                    adjacent_sym_info = sym_info
        

    def _get(self, x, y) -> str:
        if not 0 <= y < len(self.grid[0]):
            return None
        if not 0 <= x < len(self.grid):
            return None
        return self.grid[y][x]

    def _adjacent_symbol(self, x, y) -> Tuple[bool, Tuple[str, int, int]]:
        for dy, dx in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1,1)):
            val = self._get(x+dx, y+dy)
            if val is None or val == "." or val.isdigit():
                continue
            # Return success and include symbol type and location in grid
            return (True, (val, x+dx, y+dy))
        return (False, None)
            
    def part1(self) -> int:
        return sum((
            sum(nums)
            for nums in self.adj_sym_map.values()
        ))
    
    def part2(self) -> int:
        return sum((
            nums[0] * nums[1]
            for (sym, _, _), nums in self.adj_sym_map.items()
            if sym == "*" and len(nums) > 1
        ))

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    parser = Parser(lines)

    print("Part 1", parser.part1())
    print("Part 2", parser.part2())

if __name__ == "__main__":
    main()
