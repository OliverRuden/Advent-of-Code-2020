def part1() -> int:
    with open("input.txt", 'r') as f:
        l = [int(x) for x in f.read().split()]
        for idx in range(25, len(l)):
            exist = False
            for sumIdx1 in range(idx-25,idx):
                for sumIdx2 in range(sumIdx1+1, idx):
                    if l[sumIdx1] + l[sumIdx2] == l[idx]:
                        exist = True
            if not exist:
                return l[idx],l

def part2() -> int:
    goal, l = part1()
    s = 0
    i,j = 0,0
    while True:
        if s == goal and j-i >= 2:
            return max(l[i:j])+min(l[i:j])
        elif s <= goal:
            s += l[j]
            j += 1
        else: 
            s-= l[i]
            i += 1

            



def main() -> int:
    print("Part 1")
    print(part1()[0])
    print("Part 2")
    print(part2())
    return 0;

main()