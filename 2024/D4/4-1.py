def search2D(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])
    count = 0

    if grid[row][col] != word[0]:
        return count

    lenWord = len(word)

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    for dir in range(8):
        found = False
        currX, currY = row + x[dir], col + y[dir]
        k = 1

        while k < lenWord:

            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break

            if grid[currX][currY] != word[k]:
                break

            currX += x[dir]
            currY += y[dir]
            k += 1

        if k == lenWord:
            found = True

        if found:
            count += 1

    return count


def searchWord(grid, word):
    m = len(grid)
    n = len(grid[0])

    ans = []

    for i in range(m):
        for j in range(n):

            # if the word is found from this coordinate,
            # then append it to result.
            found = search2D(grid, i, j, word)
            for k in range(found):
                ans.append((i, j))

    return ans


def solve():
    grid = []
    with open('day4.txt') as my_file:
        for line in my_file:
            line_array = list(line.strip())
            grid.append(line_array)
    results = searchWord(grid, 'XMAS')

    print(len(results))


if __name__ == "__main__":
    solve()
