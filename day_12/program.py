def func1() -> int:
    direction = 90
    x,y = 0,0
    dicCard = {0:"N", 90:"E", 180:"S", 270:"W"}
    with open("input.txt",'r') as f:
        l = [(x[0],int(x[1:])) for x in f.read().split("\n")]
        for elem in l:
            d = elem[0]
            amount = elem[1]
            if d == "F":
                d = dicCard[direction]
            if d == "N":
                y += amount
            elif d == "S":
                y -= amount
            elif d == "E":
                x += amount
            elif d == "W":
                x -= amount
            elif d == "R":
                direction = (direction + amount)%360
            elif d == "L":
                direction = (direction - amount)%360
            else:
                print("Hellllpp", d)
    return abs(x) + abs(y)

def func2() -> int:
    x,y = 10,1
    xShip, yShip = 0,0
    with open("input.txt", 'r') as f:
        l = [(x[0],int(x[1:])) for x in f.read().split("\n")]
        for elem in l:
            d, amount = elem
            if d == "N":
                y += amount
            elif d == "S":
                y -= amount
            elif d == "W":
                x -= amount
            elif d == "E":
                x += amount
            elif d == "R":
                for i in range(amount//90):
                    x, y = y, -x
            elif d == "L":
                for i in range(4-amount//90):
                    x, y = y, -x
            else:
                xShip += x*amount
                yShip += y*amount
            print(x,y)
    return abs(xShip) + abs(yShip)


def main() -> int:
    print("Part 1")
    print(func1())
    print("Part 2")
    print(func2())
    return 0

main()
