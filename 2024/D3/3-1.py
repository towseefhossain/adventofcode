import re


def solve():
    total = 0
    with open('day3.txt') as my_file:
        for line in my_file:
            res = re.findall(r'mul\(([0-9]*),([0-9]*)\)', line)
            for item in res:
                total += int(item[0]) * int(item[1])
    print(total)


if __name__ == "__main__":
    solve()
