def part1() -> int:
    total = 0
    with open("input.txt", 'r') as f:
        l = f.read().split()
        idx = 0
        for row in l:
            if row[idx] == "#":
                total += 1;
            idx = (idx + 3)%len(row)
    return total;

def part2() -> int:
    testCases = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    product = 1
    with open("input.txt", 'r') as f:
        l = f.read().split()
        for elem in testCases:
            a,b = elem
            total = 0
            idx = 0
            for rowIdx in range(0,len(l),b):
                row = l[rowIdx]
                if row[idx] == "#":
                    total += 1;
                idx = (idx + a)%len(row)
            product *= total
    return product;

def main() -> int:
    print("Part 1")
    print(part1())
    print("Part 2")
    print(part2())
    return 0;

main()