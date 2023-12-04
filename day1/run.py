from functools import lru_cache
from typing import List

ALPHA_NUMS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


@lru_cache
def is_int(e: str) -> bool:
    return e.isnumeric()


@lru_cache
def get_alpha_num(line: str, start_idx: int) -> int:
    for k, v in ALPHA_NUMS.items():
        a = line.find(k, start_idx, start_idx + len(k))
        if a != -1:
            return v


def process_line1(line: str) -> List[int]:
    return [e for e in line if is_int(e)]


def part1(data: List[str]) -> List[int]:
    new_int = 0
    for line in data:
        line = line.strip()
        nums = process_line1(line)
        if not nums:
            continue
        new_int += int(nums[0] + nums[-1])
    return new_int


def process_line2(line: str) -> List[int]:
    output = []
    for idx, e in enumerate(line):
        if k := get_alpha_num(line, idx):
            output.append(k)
        elif is_int(e):
            output.append(e)
    return output


def part2(data: List[str]) -> List[int]:
    new_int = 0
    for line in data:
        line = line.strip()
        nums = process_line2(line)
        if not nums:
            continue
        k = int(nums[0] + nums[-1])
        new_int += k
    return new_int


def main():
    with open("input.txt") as fp:
        data = fp.readlines()

    result = part1(data)
    print(result)

    result = part2(data)
    print(result)


if __name__ == "__main__":
    main()
