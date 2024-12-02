def solve():
    list_a = []
    list_b = {}
    with open('day1.txt') as my_file:
        for line in my_file:
            processed_line = line.strip().split("   ")
            list_a.append(int(processed_line[0]))
            list_b[int(processed_line[-1])
                   ] = list_b.get(int(processed_line[-1]), 0) + 1

    list_a.sort()

    similarity_score = 0

    for i in list_a:
        similarity_score += list_b.get(i, 0) * i
    print(similarity_score)


if __name__ == "__main__":
    solve()
