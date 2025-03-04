import sys

from functools import reduce


def get_seeds(first_block: str) -> list[int]:
    return [int(seed) for seed in first_block.split(":")[1].split()]


class Mapper:
    def __init__(self, block: str) -> None:
        self.rows = [
            [int(number) for number in row.split()] for row in block.split("\n")[1:]
        ]

    def get_image(self, number: int):
        for row in self.rows:
            if row[1] <= number < row[1] + row[2]:
                return row[0] + number - row[1]
        return number


def resolve(data: str) -> int:
    blocks = data.split("\n\n")

    return min(
        reduce(
            lambda l, mapper: [mapper.get_image(number) for number in l],
            [Mapper(block) for block in blocks[1:]],
            get_seeds(blocks[0]),
        )
    )


def main():
    if len(sys.argv) != 2:
        print("Please specify the input file")
        return 1

    with open(sys.argv[1]) as file:
        data = file.read().strip()

    res = resolve(data)
    print(res)


if __name__ == "__main__":
    main()
