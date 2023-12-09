class RangeEntry:
        def __init__(self, lower: tuple, upper: tuple, value: int) -> None:
            self.lower = lower
            self.upper = upper
            self.value = value
        def matches(self, position: tuple):
            return (
                (position[0] >= self.lower[0]) and 
                (position[1] >= self.lower[1]) and
                (position[0] <= self.upper[0]) and 
                (position[1] <= self.upper[1])
            )
        def getValue(self):
            return self.value

class RangeMap:
    def __init__(self) -> None:
        self.entries: list[RangeEntry] = []
    def put(self, lower: tuple, upper: tuple, value: int):
        self.entries.append(RangeEntry(lower, upper, value))
    def getValueFor(self, key: tuple):
        for entry in self.entries:
            assert isinstance(entry, RangeEntry)
            if entry.matches(key):
                return entry.getValue()
        return None
        


def solve():
    line_array = []
    with open('day3.txt') as my_file:   
        for line in my_file:
            line_array.append([*(line.strip())])
    
    object_array = []
    for line in line_array:
        object_array.append(list(map(lambda x: Node(char=x), line)))
    print(object_array)
if __name__ == "__main__":
    solve()