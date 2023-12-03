from typing import List
from functools import lru_cache


@lru_cache
def is_int(e: str) -> bool:
    try:
        return int(e)
    except ValueError:
        return False


def process_line1(line: str) -> List[int]:
    return [e for e in line.strip() if is_int(e)]


def part1(data: List[str]) -> List[int]:
    new_int = 0
    for line in data:
        nums = process_line1(line)
        new_int += int(nums[0] + nums[-1])
    return new_int


def main():
    with open("input.txt") as fp:
        data = fp.readlines()

    result = part1(data)
    print(result)


if __name__ == "__main__":
    main()
