def part1() -> int:
    with open("input.txt",'r') as f:
        total = 0
        l = [x.split("\n") for x in f.read().split("\n\n")]
        for case in l:
            ansYes = set()
            for elem in case:
                ansYes |= set(elem)
            total += len(ansYes)
    return total

def part2() -> int:
    with open("input.txt",'r') as f:
        total = 0
        l = [x.split("\n") for x in f.read().split("\n\n")]
        for case in l:
            ansYes = set(case[0])
            for elem in case:
                ansYes &= set(elem)
                
            total += len(ansYes)
    return total

def main() -> int:
    print("Part 1: ")
    print(part1())
    print("Part 2:")
    print(part2())
    return 0

main()