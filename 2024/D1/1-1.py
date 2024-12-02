def solve():
    list_a = []
    list_b = []
    with open('day1.txt') as my_file:
        for line in my_file:
            processed_line = line.strip().split("   ")
            list_a.append(int(processed_line[0]))
            list_b.append(int(processed_line[-1]))

    list_a.sort()
    list_b.sort()

    diff = 0

    for i in range(len(list_a)):
        diff += abs(list_a[i] - list_b[i])
    print(diff)


if __name__ == "__main__":
    solve()
