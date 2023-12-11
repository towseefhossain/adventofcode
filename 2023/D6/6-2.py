from math import prod

def number_of_wins(time_to_distance: list):
    for t in range(1, time_to_distance[0] // 2 + 1):
        distance = t * (time_to_distance[0] - t)
        if distance > time_to_distance[1]:
            return time_to_distance[0] - (2 * t) + 1
    return 0

def solve():
    res = []
    with open('day6.txt') as file:
        for line in file:
            stripped_line = line.strip().split()[1:]
            res.append(stripped_line)

    print(res)
    times_to_distances = [int("".join(x)) for x in res]
    print(times_to_distances)
    wins = number_of_wins(times_to_distances) 
    print(wins)

if __name__ == "__main__":
    solve()