import sys

from functools import reduce


def scratchcard_value(row):
    return len(
        [
            number
            for number in row.split(":")[1].split("|")[0].split()
            if number in row.split(":")[1].split("|")[1].split()
        ]
    )


def resolve(data: str) -> int:
    return sum(
        reduce(
            lambda l, i: l[: i + 1]
            + [
                x + l[i]
                for x in l[i + 1 : i + 1 + scratchcard_value(data.split("\n")[i])]
            ]
            + l[i + 1 + scratchcard_value(data.split("\n")[i]) :],
            range(len(data.split("\n"))),
            [1] * len(data.split("\n")),
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
