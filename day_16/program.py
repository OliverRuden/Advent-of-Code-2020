import numpy as np
import queue

class Node:
    def __init__(self,LHS, ID):
        self.partners = []
        self.matches = None
        self.was = None
        self.LHS = LHS
        self.ID = ID
        self.visited = 0

def func1() -> int:
    with open("input.txt", 'r') as f:
        total = 0
        l = [x.split("\n") for x in f.read().split("\n\n")]
        instructions = []
        for elem in l[0]:
            t = [int(x) for x in elem.replace(" or ", ":").replace(" ","").replace("-",":").split(":")[-4:]]
            instructions.append([(t[0],t[1]),(t[2],t[3])])
        for elem in l[2]:
            if elem != "nearby tickets:":
                temp = [int(x) for x in elem.split(",")]
                for num in temp:
                    correct = False
                    for res in instructions:
                        a,b = res[0]
                        c,d = res[1]
                        if (a<=num<=b or c<=num<=d):
                            correct = True
                    if not correct:
                        total += num
    return total

def checkValid(temp,instructions):
    valid = {i for i in range(len(instructions))}
    for num in temp:
        tempValid = set()
        correct = False
        for idx,res in enumerate(instructions):
            a,b = res[0]
            c,d = res[1]
            if (a<=num<=b or c<=num<=d):
                correct = True
                tempValid.add(idx)
        if not correct:
            break
        valid = valid.intersection(tempValid)
    return correct, valid

def func2() -> int:
    with open("input.txt", 'r') as f:
        l = [x.split("\n") for x in f.read().split("\n\n")]
        instructions = []
        for elem in l[0]:
            t = [int(x) for x in elem.replace(" or ", ":").replace(" ","").replace("-",":").split(":")[-4:]]
            instructions.append([(t[0],t[1]),(t[2],t[3])])
        valid = []
        for elem in l[2]:
            if elem != "nearby tickets:":
                temp = [int(x) for x in elem.split(",")]
                correct, val = checkValid(temp,instructions)
                if correct:
                    valid.append(temp)
        valid = np.array(valid)
        possible = [checkValid(valid[:,i], instructions)[1] for i in range(np.shape(valid)[1])]
        nodeNumber = []
        nodeEnd = [Node(False, n) for n in range(20)]
        for idx,elem in enumerate(possible):
            nodeNumber.append(Node(True,idx))
            for i in elem:
                nodeNumber[-1].partners.append(nodeEnd[i])   
    LHS = maxMatching(nodeNumber)
    dic = {}
    for i in LHS:
        dic[i.matches.ID] = i.ID
    indexes = [idx for idx,val in enumerate(l[0]) if val.split()[0] == "departure"]
    myTicket = [int(x) for x in l[1][1].split(",")]
    prod = 1
    for place in indexes:
        prod *= myTicket[dic[place]]
    return prod

def findAugmentingPath(node,visited) -> list:
    q = queue.Queue()
    for n in node.partners:
        if n.matches == None:
            return [n, node]
        else:
            n.was = node
            n.visited = visited
            q.put(n)
    while not q.empty():
        newNode = q.get()
        for n in newNode.partners:
            if n.matches == None:
                n.was = newNode
                sol = []
                while n != None:
                    sol.append(n)
                    n = n.was
                return sol
            elif n.visited != visited:
                n.visited = visited
                n.was = newNode
                q.put(n)

def maxMatching(LHS) -> list:
    visited = 1
    sol = []
    while len(LHS) > 0:
        node = LHS.pop()
        node.visited = visited
        augmenPath = findAugmentingPath(node,visited)
        for i in range(0,len(augmenPath),2):
            augmenPath[i].matches = augmenPath[i+1]
            augmenPath[i].partners = [augmenPath[i+1]]
            augmenPath[i+1].matches = augmenPath[i]
        visited+=1
        sol.append(node)
    return sol



                

def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0;


main()

