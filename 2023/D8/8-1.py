def circular(l):
    while True:
        for item in l:
            yield item

def solve():
    directions = None
    dictionary = {}
    with open('day8.txt') as file:
        for idx, line in enumerate(file):
            if (idx == 0):
                directions = circular([int(x) for x in line.strip().replace("L", " 0 ").replace("R", " 1 ").split()])
                continue
            elif (idx == 1):
                continue
            else:
                res = line.strip().split(" = ")
                dest_tuple = tuple(res[1][1:-1].split(", "))
                dictionary[res[0]] = dest_tuple

    steps = 0
    current_object = dictionary["AAA"]
    while True:
        direction = next(directions)
        current_object = current_object[direction]
        if current_object == "ZZZ":
            break
        else:
            steps += 1
            current_object = dictionary[current_object]
    print(steps + 1)

if __name__ == "__main__":
    solve()