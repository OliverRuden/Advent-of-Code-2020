import math

def func1() -> int:
    with open("input.txt", 'r') as f:
        a = int(f.readline())
        l = [int(x) for x in f.read().split(",") if x != "x"]
        sol = [math.ceil(a/x)*x for x in l]
        i = 0
        m = sol[0]
        for idx, val in enumerate(sol):
            if val < m:
                m = val
                i = idx
    return l[i]*(sol[i]-a)

def func2() -> int:
    with open("input.txt", 'r') as f:
        a = f.readline()
        l = [int(x) if x!= "x" else 0 for x in f.read().split(",")]
        lcm = l[0]
        sol = l[0]
        for idx, val in enumerate(l):
            if idx != 0 and val != 0:
                sol,lcm = euclidAlgorithm(lcm, sol, idx, val)
    return sol

def euclidAlgorithm(lcm, val, add, n) -> int:
    newVal = n
    x = val + add
    gcd = math.gcd(x, add)
    gcd = math.gcd(gcd, n)
    x //= gcd
    n //= gcd
    y = lcm // gcd
    arr = []

    while y > 1 and n > 1:
        q, r = euclidStep(y,n)
        if y > n:
            arr.append((y,q,n,r))
            y = r
        else:
            arr.append((n,q,y,r))
            n = r
    dic = {}
    n,p,q,r = arr[-1]
    dic[r] = 1
    dic[q] = 0
    for i in range(len(arr)-1,-1,-1):
        n,p,q,r = arr[i]
        dic[n] = dic[r]
        dic[q] += -p*dic[r]
    val += lcm*((-dic[lcm//gcd]*x*gcd)%newVal)
    lcm = math.lcm(lcm, newVal)
    return val, lcm



def euclidStep(m,n):
    if m > n:
        return m//n, m-(m//n)*n
    return n//m, n-(n//m)*m


def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0;

main()