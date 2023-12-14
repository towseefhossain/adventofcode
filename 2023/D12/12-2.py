lookup_table = {}

def get_number_of_counts(symbols, sequence, sym_pos, seq_pos, curr_len):
    key = (sym_pos, seq_pos, curr_len)
    if key in lookup_table:
        return lookup_table[key]
    if (sym_pos == len(symbols)): # at the end of the symbols
        if (seq_pos == len(sequence)) and (curr_len == 0): # at the end of sequence, and we have found a valid combination previously
            return 1
        elif (seq_pos == len(sequence)-1) and (sequence[seq_pos] == curr_len): # at the end of sequence - 1, and we have found a valid combination now
            return 1
        else:
            return 0
    res = 0

    for c in ['.', '#']:
        if (symbols[sym_pos] == c) or (symbols[sym_pos] == '?'):
            if (c == '.') and (curr_len == 0):
                res += get_number_of_counts(symbols, sequence, sym_pos + 1, seq_pos, 0)
            elif (c == '.') and (curr_len > 0) and (seq_pos < len(sequence)) and (sequence[seq_pos] == curr_len):
                res += get_number_of_counts(symbols, sequence, sym_pos+1, seq_pos+1, 0)
            elif (c == '#'):
                res += get_number_of_counts(symbols, sequence, sym_pos+1, seq_pos, curr_len + 1)
    lookup_table[key] = res
    return res

def solve():
    res = 0
    with open('day12.txt') as file:
        for line in file:
            symbols, sequence = line.strip().split()
            symbols = list('?'.join([symbols, symbols, symbols, symbols, symbols]))
            sequence = sequence.split(',') * 5
            sequence = [int(x) for x in sequence]
            lookup_table.clear()
            print(symbols)
            print(sequence)
            score = get_number_of_counts(symbols, sequence, 0, 0, 0)
            res += score
    print(res)

if __name__ == "__main__":
    solve()