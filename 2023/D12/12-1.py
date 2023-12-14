import re
from alive_progress import alive_bar

def generate_all_binary_strings(bit_count: int):
    binary_strings = []
    def genbin(n, bs=''):
        if len(bs) == n:
            binary_strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')


    genbin(bit_count)
    return binary_strings

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def get_h_count(string: str):
    h_pattern = r'([\#]+)'
    matches = re.findall(h_pattern, string)
    return [len(i) for i in matches]

def get_char(i: str):
    if i == '1':
        return '#'
    else:
        return '.'

def get_count(spring: list):
    counter = 0
    binary_strings = generate_all_binary_strings(len(spring[2]))
    for bs in binary_strings:
        spring_copy = ''.join(spring[0])
        bs_list = [get_char(x) for x in list(bs)]
        zipped_list = list(zip(spring[2], bs_list))
        for item in zipped_list:
            spring_copy = replacer(spring_copy, item[1], item[0])
        
        if get_h_count(spring_copy) == spring[1]:
            counter += 1
    return counter


def solve():
    q_pattern = r'([\?])'
    springs = []
    with open('day12.txt') as file:
        for line in file:
            split = line.strip().split()
            sequence = [int(x) for x in split[1].split(",")]
            positions = [i.start(0) for i in re.finditer(q_pattern, split[0])]
            # (string, sequence, positions_of_?s)
            springs.append((split[0], sequence, positions))
    
    res = []
    with alive_bar(len(springs)) as bar:
        for spring in springs:
            res.append(get_count(spring))
            bar()

    print(sum(res))

if __name__ == "__main__":
    solve()
