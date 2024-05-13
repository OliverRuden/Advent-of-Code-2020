import numpy as np

class Node:
    def __init__(self,ID):
        self.ID = ID
        self.neighbours = set()
        self.active = False
        self.prev = False
    def update(self):
        self.prev = (self.active == True)
    def activate(self):
        c = 0
        for i in self.neighbours:
            if i.prev:
                c += 1
        if self.active:
            if c < 2 or c > 3:
                self.active = False
        elif self.active==False:
            if c == 3:
                self.active = True
        if len(self.neighbours) != 80:
            return True
        return False

def func1() -> int:
    with open("input.txt", 'r') as f:
        l = [list(x) for x in f.read().split("\n")]
        dic = {}
        k = 0
        for i in range(len(l)):
            for j in range(len(l[i])):
                tup = (i,j,k)
                node = Node(tup)
                dic[tup] = node
                node.active = (l[i][j] == "#")
        for i in range(len(l)):
            for j in range(len(l[i])):
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        for z in [-1,0,1]:
                            if abs(x)+abs(y)+abs(z) != 0:
                                tup = (i+x,j+y,z)
                                if tup not in dic:
                                    dic[tup] = Node(tup)
                                if dic[tup] not in dic[(i,j,0)].neighbours:
                                    dic[(i,j,0)].neighbours.add(dic[tup])
                                if dic[(i,j,0)] not in dic[tup].neighbours:
                                    dic[tup].neighbours.add(dic[(i,j,0)])
        newDic = dic.copy()
        for i in range(6):
            t = 0
            dic = newDic.copy()
            for val in dic.values():
                val.update()
                t += val.active
            count = 0
            for val in dic.values():
                add = val.activate()
                count += val.active
                if add:
                    for x in [-1,0,1]:
                        for y in [-1,0,1]:
                            for z in [-1,0,1]:
                                if abs(x)+abs(y)+abs(z) > 0:

                                    a,b,c = val.ID
                                    tup1 = (a,b,c)
                                    tup = (a+x,b+y,c+z)
                                    if tup not in newDic:
                                        newDic[tup] = Node(tup)
                                    newDic[tup1].neighbours.add(newDic[tup])
                                    newDic[tup].neighbours.add(newDic[tup1])
        total = 0
        for val in newDic.values():
            total += val.active
        return total

def func2() -> int:
    with open("input.txt", 'r') as f:
        l = [list(x) for x in f.read().split("\n")]
        dic = {}
        k = 0
        k2 = 0
        for i in range(len(l)):
            for j in range(len(l[i])):
                tup = (i,j,k,k2)
                node = Node(tup)
                dic[tup] = node
                node.active = (l[i][j] == "#")
        for i in range(len(l)):
            for j in range(len(l[i])):
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        for z in [-1,0,1]:
                            for k2 in [-1,0,1]:
                                if abs(x)+abs(y)+abs(z) +abs(k2)!= 0:
                                    tup = (i+x,j+y,z,k2)
                                    if tup not in dic:
                                        dic[tup] = Node(tup)
                                    if dic[tup] not in dic[(i,j,0,0)].neighbours:
                                        dic[(i,j,0,0)].neighbours.add(dic[tup])
                                    if dic[(i,j,0,0)] not in dic[tup].neighbours:
                                        dic[tup].neighbours.add(dic[(i,j,0,0)])
        newDic = dic.copy()
        for i in range(6):
            t = 0
            dic = newDic.copy()
            for val in dic.values():
                val.update()
                t += val.active
            count = 0
            for val in dic.values():
                add = val.activate()
                count += val.active
                if add:
                    for x in [-1,0,1]:
                        for y in [-1,0,1]:
                            for z in [-1,0,1]:
                                for k2 in [-1,0,1]:
                                    if abs(x)+abs(y)+abs(z) +abs(k2)> 0:
                                        a,b,c,d = val.ID
                                        tup1 = (a,b,c,d)
                                        tup = (a+x,b+y,c+z,d+k2)
                                        if tup not in newDic:
                                            newDic[tup] = Node(tup)
                                        newDic[tup1].neighbours.add(newDic[tup])
                                        newDic[tup].neighbours.add(newDic[tup1])
        total = 0
        for val in newDic.values():
            total += val.active
        return total

def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0;

main()
