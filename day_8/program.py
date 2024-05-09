def part1() -> int:
    with open("input.txt",'r') as f:
        l = [(x.split()[0],int(x.split()[1])) for x in f.read().split("\n")]
        been = [0 for i in range(len(l))]
        acc = 0
        where = 0
        while been[where] == 0:
            been[where] = 1
            inst, num = l[where]
            if inst == "jmp":
                where += num
            else:
                if inst == "acc":
                    acc += num
                where += 1
    return acc

def part2() -> int:
    with open("input.txt",'r') as f:
        lst = [(x.split()[0],int(x.split()[1])) for x in f.read().split("\n")]
        for i in range(len(lst)):
            l = lst.copy()
            if l[i][0] != "acc":
                if l[i][0] == "jmp":
                    l[i] = ("nop", l[i][1])
                else:
                    l[i] = ("jmp", l[i][1])
                been = [0 for i in range(len(l))]
                acc = 0
                where = 0
                while been[where] == 0:
                    been[where] = 1
                    inst, num = l[where]
                    if inst == "jmp":
                        where += num
                    else:
                        if inst == "acc":
                            acc += num
                        where += 1
                    if where >= len(been):
                        return acc

def main() -> int:
    print("Part 1")
    print(part1())
    print("Part 2")
    print(part2())
    return 0;

main()