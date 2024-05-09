def part1() -> int:
    total = 0
    with open("input.txt",'r') as f:
        l = f.read().split("\n\n")
        necessary = {"ecl", "pid", "byr", "iyr", "eyr", "hgt", "hcl"}
        for case in l:
            temp = set(case.replace("\n"," ").replace(":"," ").split())
            if len(necessary-temp) == 0:
                total += 1
    return total

def part2() -> int:
    total = 0
    with open("input.txt",'r') as f:
        l = f.read().split("\n\n")
        necessary  = {"ecl", "pid", "byr", "iyr", "eyr", "hgt", "hcl"}
        for case in l:
            temp = case.replace("\n"," ").replace(":"," ").split()
            tempSet = set(temp)
            dic = {}
            correct = True
            for i in range(0,len(temp), 2):
                dic[temp[i]] = temp[i+1]
            if len(necessary-tempSet) != 0:
                correct = False
            if correct:
                if not (1920<=int(dic["byr"])<=2002):
                    correct = False
                if not (2010<=int(dic["iyr"])<=2020):
                    correct = False
                if not (2020<=int(dic["eyr"])<=2030):
                    correct = False
                a = dic["hcl"]
                for i in range(len(dic["hcl"])):
                    if i == 0:
                        if a[i] != "#":
                            correct = False
                    elif i > 6:
                        correct = False
                    else:
                        if a[i] not in "0123456789abcdef":
                            correct = False
                if dic["hgt"][-2:] == "in":
                    if not (59<=int(dic["hgt"][:-2])<=76):
                        correct = False
                elif dic["hgt"][-2:] == "cm":
                    if not (150<=int(dic["hgt"][:-2])<=193):
                        correct = False
                else:
                    correct = False
                if dic["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    correct = False
                if not(len(dic["pid"]) == 9 and (dic["pid"].isnumeric())):
                    correct = False
                if correct:
                    total += 1
    return total

def main() -> int:
    print("Part 1")
    print(part1())
    print("Part 2")
    print(part2())
    return 0;

main()

