import sys
from functools import reduce

NUMBERS_DICT = {
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
NUMBERS_DICT.update(dict([(v, v) for v in NUMBERS_DICT.values()]))


def index(string: str, substring: str) -> int:
    try:
        return string.index(substring)
    except ValueError:
        return -1


def get_first_digit(positions: list[tuple[int, str]]) -> str:
    return NUMBERS_DICT[
        sorted(
            list(
                filter(
                    lambda x: x[0] != -1,
                    positions,
                )
            ),
            key=lambda y: y[0],
        )[
            0
        ][1]
    ]


def resolve(data: str) -> int:
    line = data.split()[2]

    return sum(
        [
            int(
                get_first_digit([(index(line, word), word) for word in NUMBERS_DICT])
                + get_first_digit(
                    [(index(line[::-1], word[::-1]), word) for word in NUMBERS_DICT]
                )
            )
            for line in data.split()
        ]
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
