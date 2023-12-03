import re

def solve():
    line_array = []
    with open('day1.txt') as my_file:   
        for line in my_file:
            processed_line = re.sub('\D', "", line.strip())
            number = int(processed_line[0] + processed_line[-1])
            line_array.append(number)
    print(sum(line_array))

if __name__ == "__main__":
    solve()