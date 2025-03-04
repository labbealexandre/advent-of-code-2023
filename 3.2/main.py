import sys
import re

from functools import reduce

SYMBOLS = ["#", "$", "%", "&", "*", "+", "-", "/", "=", "@"]
NUMBERS = [str(i) for i in range(10)]


def duplicate(lines: list[str]) -> list[str]:
    return [
        reduce(
            lambda d, symbol: d.replace(symbol, "s"),
            SYMBOLS,
            "".join(
                [
                    "s"
                    if lines[i - 1][j] in SYMBOLS or lines[i + 1][j] in SYMBOLS
                    else lines[i][j]
                    for j in range(len(lines[i]))
                ]
            ),
        )
        for i in range(1, len(lines) - 1)
    ]


def sum_ints(string: str) -> int:
    return sum(
        [
            int(char)
            for char in re.findall(
                r"\.(\d+)\.",
                ("." + string + ".").replace(".", ".."),
            )
        ]
    )


def resolve(data: str) -> int:
    return sum_ints(
        "".join([char if char.isnumeric() else "." for char in ".".join(data.split())])
    ) - sum_ints(
        ".".join(
            duplicate(
                ["." * len(data.split())] + data.split() + ["." * len(data.split())]
            )
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
