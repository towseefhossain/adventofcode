import pprint

pp = pprint.PrettyPrinter()

class Node:
    def __init__(self, index: int) -> None:
        self.children: list[Node] = []
        self.index = index

    def add_child(self, node):
        self.children.append(node)

    def add_children(self, node_list: list):
        for child in node_list:
            self.children.append(child)

    def sum_children(self):
        if self is None:
            return 0
        if self.children == []:
            return 1
        else:
            res_array = [x.sum_children() for x in self.children if x is not None]
            return 1 + sum(res_array)
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.index)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

def find_children(winning_numbers, my_numbers, index):
    children = []
    curr = index
    for number in winning_numbers:
        if number in my_numbers:
            children.append(curr + 1)
            curr += 1
    return children

def recurse(index, children, lookup_table) -> Node:
    root = Node(index)
    if (children == []):
        return root
    else:
        for child in children:
            root.add_child(recurse(child, lookup_table[child], lookup_table))
        return root

def solve():
    line_array = []
    with open('day4.txt') as my_file:   
        for (idx, line) in enumerate(my_file):
            first_split = line.strip().replace(': ', '&').replace(' | ', '&').split('&')
            res = find_children(first_split[1].split(), first_split[2].split(), idx)
            line_array.append(res)

    null_node = Node(-1)
    for (idxx, line) in enumerate(line_array):
        null_node.add_child(recurse(idxx, line, line_array))

    print(null_node.sum_children() - 1)

if __name__ == "__main__":
    # print(find_children('41 48 83 86 17'.split(), '83 86  6 31 17  9 48 53'.split(), 0))
    # assert calculate_score('41 48 83 86 17'.split(), '83 86  6 31 17  9 48 53'.split()) == 8, f'is actually {calculate_score("41 48 83 86 17".split(), "83 86  6 31 17  9 48 53".split())}'
    # assert calculate_score('13 32 20 16 61'.split(), '61 30 68 82 17 32 24 19'.split()) == 2, f'is actually {calculate_score("13 32 20 16 61".split(), "61 30 68 82 17 32 24 19".split())}'
    # assert calculate_score(' 1 21 53 59 44'.split(), '69 82 63 72 16 21 14  1'.split()) == 2, f'is actually {calculate_score(" 1 21 53 59 44".split(), "69 82 63 72 16 21 14  1".split())}'
    # assert calculate_score('41 92 73 84 69'.split(), '59 84 76 51 58  5 54 83'.split()) == 1, f'is actually {calculate_score("41 92 73 84 69".split(), "59 84 76 51 58  5 54 83".split())}'
    # assert calculate_score('87 83 26 28 32'.split(), '88 30 70 12 93 22 82 36'.split()) == 0, f'is actually {calculate_score("87 83 26 28 32".split(), "88 30 70 12 93 22 82 36".split())}'
    # assert calculate_score('31 18 13 56 72'.split(), '74 77 10 23 35 67 36 11'.split()) == 0, f'is actually {calculate_score("31 18 13 56 72".split(), "74 77 10 23 35 67 36 11".split())}'
    
    # assert copy_number('41 48 83 86 17'.split(), '83 86  6 31 17  9 48 53'.split()) == 4, f'is actually {copy_number("41 48 83 86 17".split(), "83 86  6 31 17  9 48 53".split())}'
    
    solve()
