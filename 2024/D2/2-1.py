def generateDifferences(listOfInts):
    differences = []
    for i in range(len(listOfInts) - 1):
        diff = int(listOfInts[i]) - int(listOfInts[i + 1])
        differences.append(diff)
    return differences


def isSafe(listOfInts):
    listOfDifferences = generateDifferences(listOfInts)
    if all(difference > 0 for difference in listOfDifferences) or all(difference < 0 for difference in listOfDifferences):
        if ((all(abs(difference) >= 1 for difference in listOfDifferences)) and (all(abs(difference) <= 3 for difference in listOfDifferences))):
            return True
    return False


def solve():
    safeLists = []
    with open('day2.txt') as my_file:
        for line in my_file:
            processed_line = line.strip().split(" ")
            if isSafe(processed_line):
                safeLists.append(processed_line)
            else:
                for index in range(len(processed_line)):
                    removedList = processed_line[:index] + \
                        processed_line[index+1:]
                    if isSafe(removedList):
                        safeLists.append(processed_line)
                        break
            print(len(safeLists))


if __name__ == "__main__":
    solve()
