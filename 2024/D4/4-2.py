
def isValid(matrix):
    if (matrix[0][0] == 'M'):
        if (matrix[0][2] == 'M'):
            if (matrix[1][1] == 'A'):
                if (matrix[2][0] == 'S'):
                    if (matrix[2][2] == 'S'):
                        return True
    return False


def rotate(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]


def search2D(grid):
    m = len(grid)
    n = len(grid[0])
    count = 0

    for i in range(m-2):
        for j in range(n-2):
            matrix = [grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]
            numRotations = 4
            while numRotations != 0:
                if isValid(matrix):
                    count += 1
                    break
                matrix = rotate(matrix)
                numRotations -= 1
    return count


def searchWord(grid):
    count = search2D(grid)
    return count


def solve():
    grid = []
    with open('day4.txt') as my_file:
        for line in my_file:
            line_array = list(line.strip())
            grid.append(line_array)
    results = searchWord(grid)

    print(results)


if __name__ == "__main__":
    solve()
