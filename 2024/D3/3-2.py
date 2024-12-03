import re


def solve():
    total = 0
    with open('day3.txt') as my_file:
        total_line = ''
        for line in my_file:
            total_line += line.strip()
        modded_line = re.sub(r'(?<=don\'t\(\)).*?(?=do\(\))', '', total_line)
        res = re.findall(r'mul\(([0-9]*),([0-9]*)\)', modded_line)
        for item in res:
            total += int(item[0]) * int(item[1])
    print(total)


if __name__ == "__main__":
    solve()
