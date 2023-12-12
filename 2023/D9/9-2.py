def all_zero(lst):
    for item in lst:
        if item != 0:
            return False
    return True

def get_previous(lst):
    to_be_added = None
    differences = [j-i for i, j in zip(lst[:-1], lst[1:])]
    if all_zero(differences):
        to_be_added = differences[0]
    else:
        to_be_added = get_previous(differences)
    return lst[0] - to_be_added

def solve():
    input_array = []
    with open('day9.txt') as file:
        for line in file:
            x = [int(x) for x in line.strip().split()]
            input_array.append(x)
    
    res = list(map(lambda x: get_previous(x), input_array))
    print(sum(res))

if __name__ == "__main__":
    solve()