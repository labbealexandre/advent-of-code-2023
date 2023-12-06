import sys


def resolve(data: str) -> int:
    return sum(
        [
            int(y[0] + y[-1])
            for y in [
                list(
                    filter(
                        lambda x: x.isnumeric(),
                        [char for char in list(line)],
                    )
                )
                for line in data.split()
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
