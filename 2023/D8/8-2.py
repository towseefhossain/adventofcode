import math
from functools import reduce

def lcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

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
                directions = [int(x) for x in line.strip().replace("L", " 0 ").replace("R", " 1 ").split()]
                continue
            elif (idx == 1):
                continue
            else:
                res = line.strip().split(" = ")
                dest_tuple = tuple(res[1][1:-1].split(", "))
                dictionary[res[0]] = dest_tuple

    all_starting_objects = [x for x in list(dictionary.keys()) if x[-1] == 'A']
    steps_array = []
    for starting_object in all_starting_objects:
        steps = 0
        current_object = dictionary[starting_object]
        true_directions = circular(directions)
        while True:
            direction = next(true_directions)
            current_object = current_object[direction]
            if current_object[-1] == "Z":
                break
            else:
                steps += 1
                current_object = dictionary[current_object]
        steps_array.append(steps + 1)
    print(lcm(steps_array))

if __name__ == "__main__":
    solve()