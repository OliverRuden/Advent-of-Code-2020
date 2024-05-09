def part1() -> int:
    with open ("input.txt", 'r') as f:
        l = sorted([int(x) for x in f.read().split("\n")])
        for num in l:
            i = 0
            j = len(l)
            while i < j:
                p = (i+j)//2
                if num + l[p] < 2020:
                    i = p+1
                elif num+l[p] > 2020:
                    j = p
                else:
                    return num * l[p]
    return 0

def part2() -> int:
    with open ("input.txt", 'r') as f:
        l = sorted([int(x) for x in f.read().split("\n")])
        for idx,num in enumerate(l):
            for num1 in l[idx+1:]:
                i = 0
                j = len(l)
                while i < j:
                    p = (i+j)//2
                    if num+num1 + l[p] < 2020:
                        i = p+1
                    elif num+num1+l[p] > 2020:
                        j = p
                    else:
                        return num * num1 * l[p]
    return 0

def main() -> int:
    print("Part 1")
    print(part1())
    print("Part 2")
    print(part2())
    return 0

main()

        
