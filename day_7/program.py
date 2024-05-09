class Node:
    def __init__(self, name):
        self.name = name;
        self.isGold = False
        self.parent = set()
        self.visited = 0
        self.children = set()


def DFS(node, dic) -> int:
    if node.isGold:
        total = 0
        node.visited = 0
        node.isGold = False
    else:
        total = 1
        node.visited = 1
    for parent1 in node.parent:
        parent = dic[parent1]
        if not parent.visited:
            total += DFS(parent, dic)
    return total;

def part1() -> int:
    with open("input.txt",'r') as f:
        l = [x.replace("contain",",").split(",") for x in f.read().split("\n")]
        dic = {}
        for elem in l:
            colors = []
            for idx, color in enumerate(elem):
                if idx == 0:
                    colors.append(" ".join(color.split()[:-1]))
                else:
                    colors.append(" ".join(color.split()[1:-1]))
            for idx, color in enumerate(colors):
                if color not in dic:
                    dic[color] = Node(color)
                if idx != 0:
                    dic[color].parent.add(colors[0])
    dic["shiny gold"].isGold = True
    return DFS(dic["shiny gold"], dic);

def DFS2(node, dic):
    if node.name == "shiny gold":
        total = 0
    else:
        total = 1
    for tup in node.children:
        amount, children = tup
        child = dic[children]
        total += amount*DFS2(child,dic)
    return total


    

def part2() -> int:
    with open("input.txt",'r') as f:
        l = [x.replace("contain",",").split(",") for x in f.read().split("\n")]
        dic = {}
        for elem in l:
            colors = []
            for idx, color in enumerate(elem):
                colors.append(color.split()[:-1])
            for idx, color in enumerate(colors):
                if color[0] != "no":
                    if idx != 0:
                        amount = int(color[0])
                        name = " ".join(color[1:])
                    else:
                        name = " ".join(color)
                    if name not in dic:
                        dic[name] = Node(name)
                    if idx != 0:
                        dic[" ".join(colors[0])].children.add((amount, name))
    return DFS2(dic["shiny gold"], dic);

def main() -> int:
    print("Part 1")
    print(part1())
    print("Part 2")
    print(part2())
    return 0

main()