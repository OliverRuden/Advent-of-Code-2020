def op(i1,sgn,i2):
    if sgn == "*":
        return i1*i2
    elif sgn == "+":
        return i1+i2
    raise Exception("Something is wrong")

def noBrac(lis):
    a = int(lis[0])
    for i in range(1,len(lis),2):
        a = op(a,lis[i],int(lis[i+1]))
    return a

def func1() -> int:
    with open("input.txt",'r') as f:
        total = 0
        l = [x.replace("(","( ").replace(")"," )").split() for x in f.read().split("\n")]
        for line in l:
            i = 0
            while i < len(line)-1:
                bracIdx = []
                c = line.copy()
                for i in range(0,len(line)):
                    if line[i] == "(":
                        bracIdx.append(i)
                    elif line[i] == ")":
                        idx = bracIdx[-1]
                        val = noBrac(line[idx+1:i])
                        c = line[:idx] + [val] + line[i+1:]
                        i -= (i+2-idx)
                        break
                line = c.copy()
            total += noBrac(line)
    return total

def func2() -> int:
    with open("input.txt",'r') as f:
        total = 0
        l = [x.replace("(","( ").replace(")"," )").split() for x in f.read().split("\n")]
        for line in l:
            i = 0
            while i < len(line)-1:
                bracIdx = []
                c = line.copy()
                for i in range(0,len(line)):
                    if line[i] == "(":
                        bracIdx.append(i)
                    elif line[i] == ")":
                        idx = bracIdx[-1]
                        val = noBrac2(line[idx+1:i])
                        c = line[:idx] + [val] + line[i+1:]
                        i -= (i+2-idx)
                        break
                line = c.copy()
            total += int(noBrac2(line))
    return total

def find(s,lis) -> int:
    for idx,val in enumerate(lis):
        if val == "+":
            return idx
    return None

def noBrac2(lis):
    foundIdx = find("+",lis)
    while foundIdx:
        lis = lis[:foundIdx-1] + [str(int(lis[foundIdx-1])+int(lis[foundIdx+1]))] + lis[foundIdx+2:]
        foundIdx = find("+",lis)
    return str(eval("".join(lis)))

def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    
main()



