def convert(string) -> int:
    row = ""
    for j in range(7):
        if string[j] == "B":
            row += "1"
        else:
            row+= "0"
    column = ""
    for j in range(7,10):
        if string[j] == "R":
            column += "1"
        else:
            column+= "0"
    return int(row,2)*8+int(column,2)

def func1() -> int:
    m = 0
    with open("input.txt", 'r') as f:
        l = f.read().split("\n")
        for i in l:
            num = convert(i)
            if num > m:
                m = num
    return m

def func2() -> int:
    with open("input.txt", 'r') as f:
        l = f.read().split("\n")
        seat = []
        for i in l:
            num = convert(i)
            seat.append(num)
        seat.sort()
        i = 0
        j = len(seat)
        while i < j:
            p = (i+j)//2
            if seat[p]-seat[0]==p:
                i = p
            elif seat[p-1]-seat[0]==p-1:
                return seat[p]-1
            else:
                j = p

def main()->int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0;

main()