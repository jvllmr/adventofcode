import os
from string import ascii_letters


def get_rucksacks(lines: list[str]) -> list[tuple[str, str]]:
    line_gen = (line.strip() for line in lines)
    return [
        (line[: len(line) // 2], line[len(line) // 2 :])  # noqa: E203
        for line in line_gen
    ]


def group_rucksacks(
    rucksacks: list[tuple[str, str]], group_size=3
) -> list[list[tuple[str, str]]]:
    res = []
    rucksacks = rucksacks.copy()
    while rucksacks:
        group = []
        for _ in range(0, group_size):
            if rucksacks:
                group.append(rucksacks.pop())
        res.append(group)
    return res


def shared_items(rucksack: tuple[str, str]) -> set[str]:
    first_compartment, second_compartment = rucksack
    return set(first_compartment).intersection(second_compartment)


def shared_group_items(rucksack_group: list[tuple[str, str]]):
    shared_items = set(ascii_letters)
    for rucksack in rucksack_group:
        first_compartment, second_compartment = rucksack
        shared_items.intersection_update(first_compartment + second_compartment)

    return shared_items


def item_value(item: str):
    return ascii_letters.index(item) + 1


def main():
    with open(os.path.dirname(__file__) + "/input.txt", "r") as f:
        lines = f.readlines()

        rucksacks = get_rucksacks(lines)
        shared_rucksack_items = [shared_items(rucksack) for rucksack in rucksacks]

        print(sum(map(lambda x: item_value(x.pop()), shared_rucksack_items)))

        grouped_rucksacks = group_rucksacks(rucksacks)

        print(
            sum(
                map(
                    lambda x: item_value(x.pop()),
                    (
                        shared_group_items(rucksack_group)
                        for rucksack_group in grouped_rucksacks
                    ),
                )
            )
        )


if __name__ == "__main__":
    main()
