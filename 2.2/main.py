import sys


def extract_int(string: str) -> int:
    return int("".join(list(filter(lambda char: char.isnumeric(), list(string)))))


def max_color(elements: list[str], color: str):
    return max([extract_int(s) for s in list(filter(lambda e: color in e, elements))])


def resolve(data: str) -> int:
    return sum(
        [
            max_color(z[1], "red") * max_color(z[1], "green") * max_color(z[1], "blue")
            for z in [
                (
                    int(line.split(":")[0].split()[1]),
                    line.split(":")[1].replace(";", ",").split(","),
                )
                for line in data.split("\n")
            ]
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
