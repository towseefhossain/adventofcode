a = [
    '0ksajldklajsdlksad',
    '1ksajdlsakjdlkaskj',
    '2dkjfdlksjflksdjff',
    '3fkldsjfkdlskdfsjs',
    '4ksajldklajsdlksad',
    '5ksajdlsakjdlkaskj',
    '6dkjfdlksjflksdjff',
    '7fkldsjfkdlskdfsjs',
]

def get_horizontal(arr: list, bias: int, isVertical = False) -> int:
    length = len(arr)
    if length < 2:
        return 0
    if length % 2 != 0:
        return max(
            0,
            get_horizontal(arr[1:], bias + 1),
            get_horizontal(arr[:-1], bias)
        )
    if (arr[:length//2] == arr[length:length//2 - 1:-1]):
        if (isVertical): 
            return length//2 + 1
        else:
            return length//2 + bias
    else:
        return max(
            0,
            get_horizontal(arr[1:], bias + 1),
            get_horizontal(arr[:-1], bias)
        )

def get_vertical(arr: list) -> int:
    rotated_arr = list(zip(*arr[::-1]))
    
    return get_horizontal(rotated_arr, 0, isVertical=True) 

def solve():
    with open('day13-example.txt') as file:
        map = []
        score = 0
        for line in file:
            if line.strip() == "":
                horizontal = get_horizontal(map, 0)
                vertical = get_vertical(map)
                if horizontal >= vertical:
                    score += horizontal * 100
                    print(f'horizontal found {horizontal}, vertical was {vertical}, score is now {score}')
                else:
                    score += vertical
                    print(f'vertical found {vertical}, horizontal was {horizontal}, score is now {score}')
                map = []
            else:
                map.append(line.strip())
        horizontal = get_horizontal(map, 0)
        vertical = get_vertical(map)
        if horizontal >= vertical:
            score += horizontal * 100
            print(f'horizontal found {horizontal}, vertical was {vertical}, score is now {score}')
        else:
            score += vertical
            print(f'vertical found {vertical}, horizontal was {horizontal}, score is now {score}')
         
    print(score)

if __name__ == "__main__":
    # x = len(a)
    # print(a[x:x//2 - 1:-1])
    # print([a[-1]] + a)
    solve()