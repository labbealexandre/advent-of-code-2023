import sys


def resolve(data: str) -> int:
    return sum(
        [
            2 ** (count - 1)
            for count in [
                len(
                    [
                        number
                        for number in row.split(":")[1].split("|")[0].split()
                        if number in row.split(":")[1].split("|")[1].split()
                    ]
                )
                for row in data.split("\n")
            ]
            if count > 0
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
