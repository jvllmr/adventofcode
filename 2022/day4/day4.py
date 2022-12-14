import os


def get_range(range_str: str):
    start, stop = range_str.split("-")
    return range(int(start), int(stop) +1)


def get_ranges(lines: list[str]) -> list[tuple[range, range]]:
    pairs = []

    for line in lines:
        range_str_1, range_str_2 = line.strip().split(",")
        pairs.append((get_range(range_str_1), get_range(range_str_2)))

    return pairs


def range_contains_other(range_: range, range_2: range) -> bool:
    return (range_.start >= range_2.start and range_.stop <= range_2.stop) or (
        range_.start <= range_2.start and range_.stop >= range_2.stop
    )


def ranges_overlap(range_: range, range_2: range) -> bool:
    return bool(set(range_2).intersection(range_))


def main():
    with open(os.path.dirname(__file__) + "/input.txt", "r") as f:
        lines = f.readlines()

    pairs = get_ranges(lines)
    
    print(
        sum(1 for range_1, range_2 in pairs if range_contains_other(range_1, range_2))
    )
    
    print(sum(1 for range_1, range_2 in pairs if ranges_overlap(range_1, range_2)))


if __name__ == "__main__":
    main()
