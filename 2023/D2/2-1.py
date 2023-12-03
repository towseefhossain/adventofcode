import pprint
pp = pprint.PrettyPrinter()


def solve(red: int, blue: int, green: int):
    limits = {
        "red": red,
        "blue": blue,
        "green": green
    }

    line_array = []
    with open('day2.txt') as my_file:
        for line in my_file:
            split = line.strip().split(": ")
            new_line = list(map(lambda x: x.split(", "), split[1].split("; ")))
            line_array.append(new_line)

        invalidGames = set()
        for (idx, line) in enumerate(line_array):
            for game in line:
                for item in game:
                    split = item.split(" ")
                    if int(split[0]) > limits[split[1]]:
                        print(f'{split}')
                        invalidGames.add(idx+1)
        
        allGames = [i for i in range(1,101)]
        validGames = set(allGames) - set(invalidGames)
        print(sum(validGames))

if __name__ == "__main__":
    solve(12,14,13)