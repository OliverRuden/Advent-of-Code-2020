def func1() -> int:
    dic = {}
    with open("input.txt",'r') as f:
        l = [int(x) for x in f.read().split(",")]
        for idx, val in enumerate(l):
            dic[val] = idx+1
        spoken = len(l)+1
        current = 0
        while spoken < 2020:
            if current in dic:
                temp = current
                current = spoken-dic[current]
                dic[temp] = spoken
            else:
                dic[current] = spoken
                current = 0
            spoken += 1
    return current

def func2() -> int:
    dic = {}
    with open("input.txt",'r') as f:
        l = [int(x) for x in f.read().split(",")]
        for idx, val in enumerate(l):
            dic[val] = idx+1
        spoken = len(l)+1
        current = 0
        while spoken < 30000000:
            if current in dic:
                temp = current
                current = spoken-dic[current]
                dic[temp] = spoken
            else:
                dic[current] = spoken
                current = 0
            spoken += 1
    return current

def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0;


main()

