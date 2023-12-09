def calculate_score(winning_numbers, my_numbers):
    power_of_two = -1
    for number in winning_numbers:
        if number in my_numbers:
            power_of_two += 1
    
    if power_of_two == -1:
        return 0 
    else:
        return 2**power_of_two

def solve():
    line_array = []
    with open('day4.txt') as my_file:   
        for line in my_file:
            first_split = line.strip().replace(': ', '&').replace(' | ', '&').split('&')
            inputs = [first_split[1].split(), first_split[2].split()]
            res = calculate_score(inputs[0], inputs[1])
            line_array.append(res)

    print(sum(line_array))

if __name__ == "__main__":
    assert calculate_score('41 48 83 86 17'.split(), '83 86  6 31 17  9 48 53'.split()) == 8, f'is actually {calculate_score("41 48 83 86 17".split(), "83 86  6 31 17  9 48 53".split())}'
    assert calculate_score('13 32 20 16 61'.split(), '61 30 68 82 17 32 24 19'.split()) == 2, f'is actually {calculate_score("13 32 20 16 61".split(), "61 30 68 82 17 32 24 19".split())}'
    assert calculate_score(' 1 21 53 59 44'.split(), '69 82 63 72 16 21 14  1'.split()) == 2, f'is actually {calculate_score(" 1 21 53 59 44".split(), "69 82 63 72 16 21 14  1".split())}'
    assert calculate_score('41 92 73 84 69'.split(), '59 84 76 51 58  5 54 83'.split()) == 1, f'is actually {calculate_score("41 92 73 84 69".split(), "59 84 76 51 58  5 54 83".split())}'
    assert calculate_score('87 83 26 28 32'.split(), '88 30 70 12 93 22 82 36'.split()) == 0, f'is actually {calculate_score("87 83 26 28 32".split(), "88 30 70 12 93 22 82 36".split())}'
    assert calculate_score('31 18 13 56 72'.split(), '74 77 10 23 35 67 36 11'.split()) == 0, f'is actually {calculate_score("31 18 13 56 72".split(), "74 77 10 23 35 67 36 11".split())}'
    solve()
