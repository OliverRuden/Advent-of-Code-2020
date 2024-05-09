def part1() -> int:
    with open("input.txt", 'r') as f:
        l = [list(x) for x in f.read().split("\n")]
        newLoop = True
        while newLoop:
            newLoop = False
            new = [["." for i in range(len(l[0]))] for j in range(len(l))]
            for i in range(len(l)):
                for j in range(len(l[i])):
                    new[i][j] = l[i][j]
            for i in range(len(l)):
                for j in range(len(l[i])):
                    if l[i][j] != ".":
                        c = 0
                        for k in [-1,0,1]:
                            for w in [-1,0,1]:
                                if 0<=i+k<len(l) and 0<=j+w<len(l[i]):
                                    if l[i+k][j+w] == "#":
                                        c+=1
                        if l[i][j] == "L":
                            if c == 0:
                                newLoop = True
                                new[i][j] = "#"
                        else:
                            if c > 4:
                                newLoop = True
                                new[i][j] = "L"
            l = new
    total = 0
    for i in l:
        for j in i:
            if j == "#":
                total += 1
    return total

def add(i) -> int:
    if i > 0:
        return i + 1
    elif i < 0:
        return i - 1
    return 0

def part2() -> int:
    with open("input.txt", 'r') as f:
        l = [list(x) for x in f.read().split("\n")]
        newLoop = True
        while newLoop:
            newLoop = False
            new = [["." for i in range(len(l[0]))] for j in range(len(l))]
            for a in range(len(l)):
                for b in range(len(l[a])):
                    new[a][b] = l[a][b]
            for i in range(len(l)):
                for j in range(len(l[i])):
                    if l[i][j] != ".":
                        c = 0
                        for idx1 in [-1,0,1]:
                            for idx2 in [-1,0,1]:
                                k,w = idx1,idx2
                                while True:
                                    if 0<=i+k<len(l) and 0<=j+w<len(l[i+k]):
                                        if l[i+k][j+w] == "#":
                                            c+=1
                                            break
                                        elif l[i+k][j+w] == "L":
                                            break
                                        k = add(k)
                                        w = add(w)
                                    else:
                                        break
                        if l[i][j] == "L":
                            if c == 0:
                                newLoop = True
                                new[i][j] = "#"
                        else:
                            if c > 5:
                                newLoop = True
                                new[i][j] = "L"
            l = new

    total = 0
    for i in l:
        for j in i:
            if j == "#":
                total += 1
    return total

def main() -> int:
    print("Part 1")
    print(part1())
    print("Part 2")
    print(part2())
    return 0;

main()
    



