import pprint
pp = pprint.PrettyPrinter()


def solve():
    line_array = []
    with open('day2.txt') as my_file:
        for line in my_file:
            split = line.strip().split(": ")
            new_line = list(map(lambda x: x.split(", "), split[1].split("; ")))
            line_array.append(new_line)

        gameScores = [0 for i in range(0, len(line_array))]
        for (idx, line) in enumerate(line_array):
            maxes = {
                'red': 0,
                "blue": 0,
                "green": 0
            }
            for game in line:
                for item in game:
                    split = item.split(" ")
                    if int(split[0]) > maxes[split[1]]:
                        maxes[split[1]] = int(split[0])
                print(maxes)
            gameScores[idx] = maxes["red"] * maxes["blue"] * maxes["green"]
        
        
        print(sum(gameScores))

if __name__ == "__main__":
    solve()