import re

def solve():
    line_array = []
    word_to_number_mapping = ['zero','one','two','three','four','five','six','seven','eight','nine']
    with open('day1.txt') as my_file:   
        for line in my_file:
            processed_line = line.strip()
            for i in range(1, len(processed_line)):
                front_half = processed_line [0: i]
                back_half = processed_line[i:]
                for i in range(0,10):
                    front_half = re.sub(word_to_number_mapping[i], word_to_number_mapping[i][0] + str(i) + word_to_number_mapping[i][-1], front_half)
                processed_line = front_half + back_half
            final_pass = processed_line
            for i in range(0,10):
                final_pass = re.sub(word_to_number_mapping[i], word_to_number_mapping[i][0] + str(i) + word_to_number_mapping[i][-1], final_pass)
            processed_line = re.sub('\D', "", final_pass)
            number = int(processed_line[0] + processed_line[-1])
            line_array.append(number)
    print(sum(line_array))

if __name__ == "__main__":
    solve()