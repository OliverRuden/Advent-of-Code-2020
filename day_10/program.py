def func1() -> int:
    jumps = [0,0,1]
    current = 0
    with open("input.txt",'r') as f:
        l = [int(x) for x in f.read().split("\n")]
        l.sort()
        for i in l:
            jumps[i-current-1] += 1
            current = i
    return jumps[0]*jumps[2]

def func2():
    dynProg = [1]
    with open("input.txt",'r') as f:
        l = [int(x) for x in f.read().split("\n")]
        l.append(0)
        l.sort()
        for idx, val in enumerate(l):
            if idx != 0:
                dynProg.append(0)
            tempIdx = idx-1
            while tempIdx >= 0:
                if val - l[tempIdx] <= 3:
                    dynProg[-1] += dynProg[tempIdx]
                    tempIdx -= 1
                else:
                    break
    return dynProg[-1]


def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0;

main()