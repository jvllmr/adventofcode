import os


def get_elves(lines: list[str]) -> list[list[int]]:
    elves: list[list[int]] = []
    elf: list[int] = []
    for line in lines:
        line = line.strip()
        if line:
            elf.append(int(line))
        else:
            elves.append(elf)
            elf = []

    return elves


def get_max_elf_calories(elves: list[list[int]]) -> int:
    return max(map(sum, elves))


def sort_elves_by_total_calories(elves: list[list[int]]):
    sorted_elves = elves.copy()

    def get_elf_key(elf: list[int]):
        return sum(elf)

    sorted_elves.sort(key=get_elf_key, reverse=True)
    return sorted_elves


def main():
    with open(os.path.dirname(__file__) + "/input.txt", "r") as f:
        lines = f.readlines()

    elves = get_elves(lines)

    print(get_max_elf_calories(elves))

    sorted_elves = sort_elves_by_total_calories(elves)
    top_three_elves = sorted_elves[:3]
    print(sum(sum(top_three_elves, [])))


if __name__ == "__main__":
    main()
