def part1() -> int:
    total = 0
    with open("input.txt") as f:
        l = [i.split(" ") for i in f.read().split("\n")]
        for case in l:
            c = case[2].count(case[1][0])
            border = case[0].split("-")
            if int(border[0]) <= c <= int(border[1]):
                total += 1
    return total;

def part2() -> int:
    total = 0
    with open("input.txt") as f:
        l = [i.split(" ") for i in f.read().split("\n")]
        for case in l:
            border = case[0].split("-")
            if (case[2][int(border[0])-1]==case[1][0]) + (case[2][int(border[1])-1]==case[1][0]) == 1:
                total += 1
    return total;
def main() -> int:
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
    return 0;

main()
