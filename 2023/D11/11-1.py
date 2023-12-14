import pprint

pp = pprint.PrettyPrinter()

def calculate_steps(galaxy_a: tuple, galaxy_b: tuple):
    x_dist = abs(galaxy_a[1][0] - galaxy_b[1][0])
    y_dist = abs(galaxy_a[1][1] - galaxy_b[1][1])
    return x_dist + y_dist

def generate_pair(list):
    res = []
    for idx_a, item_a in enumerate(list):
        for item_b in list[idx_a+1:]:
            res.append((item_a, item_b))
    return res 

def expand_rows(arr: list, row_labels: list) -> dict:
    for idx_r, row in enumerate(arr):
        if (set(row) == {'.'}):
            to_be_updated = list(filter(lambda x: x[0] > idx_r, row_labels))
            updated_list = list(filter(lambda x: x[0] <= idx_r, row_labels))
            for item in to_be_updated:
                updated_list.append((item[0], item[1] + 1))
            row_labels = updated_list
    return dict(row_labels)

def expand_cols(arr: list, col_labels: list) -> dict:
    rotated_arr = []
    for i in range(0, len(arr[0])):
        col = [x[i] for x in arr]
        rotated_arr.append(col)
    for idx_c, col in enumerate(rotated_arr):
        if (set(col) == {'.'}):
            to_be_updated = list(filter(lambda x: x[0] > idx_c, col_labels))
            updated_list = list(filter(lambda x: x[0] <= idx_c, col_labels))
            for item in to_be_updated:
                updated_list.append((item[0], item[1] + 1))
            col_labels = updated_list
    return dict(col_labels)

def solve():
    arr = []
    with open('day11.txt') as file:
        for line in file:
            arr.append(list(line.strip()))
    
    row_labels = [(i, i)for i in range(0, len(arr))]
    col_labels = [(i, i)for i in range(0, len(arr[0]))]

    row_map = expand_rows(arr, row_labels)
    col_map = expand_cols(arr, col_labels)

    num_galaxies = 0
    galaxy_mapping = {}
    for idx_r, row in enumerate(arr):
        for idx_c, item in enumerate(row):
            if item == "#":
                num_galaxies += 1
                arr[idx_r][idx_c] = num_galaxies
                galaxy_mapping[num_galaxies] = (row_map[idx_r], col_map[idx_c])

    pairs = generate_pair(list(galaxy_mapping.items()))
    steps = [calculate_steps(x[0], x[1]) for x in pairs]

    print(sum(steps))


if __name__ == "__main__":
    solve()