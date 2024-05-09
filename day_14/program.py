def func1() -> int:
    dic = {}
    with open("input.txt",'r') as f:
        l = f.read().split("\n")
        for string in l:
            if string[:4] == "mask":
                bitmask = string.split()[2]
            else:
                elems = string.replace("["," ").replace("]", " ").split()
                mem = int(elems[1])
                num = bin(int(elems[3]))[2:]
                s = ""
                for idx in range(len(bitmask)):
                    if bitmask[idx] != "X":
                        s+=bitmask[idx]
                    elif 35-idx < len(num):
                        s+=num[len(num)+idx-36]
                    else:
                        s+="0"
                dic[mem] = int(s,2)
    total = 0
    for key,val in dic.items():
        total += val
    return total

def getAllMem(s, idx, bitmask,mem):
    sol = []
    for i in range(idx, len(bitmask)):
        if bitmask[i] == "0":
            s += mem[i]
        elif bitmask[i] == "1":
            s += "1"
        else:
            sol = getAllMem(s+"1",i+1,bitmask,mem)
            sol.extend(getAllMem(s+"0",i+1,bitmask,mem))
            break
    if len(sol) == 0:
        sol = [s]
    return sol

def func2() -> int:
    dic = {}
    with open("input.txt",'r') as f:
        l = f.read().split("\n")
        for string in l:
            if string[:4] == "mask":
                bitmask = string.split()[2]
            else:
                elems = string.replace("["," ").replace("]", " ").split()
                mem = bin(int(elems[1]))[2:]
                mem = (36-len(mem))*"0" + mem   
                num = int(elems[3])
                s = ""
                adresses = getAllMem(s,0, bitmask, mem)
                for memory in adresses:
                    dic[memory] = num
    total = 0
    for key,val in dic.items():
        total += val
    return total

def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0;

main()