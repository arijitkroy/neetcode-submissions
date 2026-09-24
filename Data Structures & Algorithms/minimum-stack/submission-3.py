class MinStack:

    def __init__(self):
        self.arr = []
        self.m = float('inf')

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.m = min(self.arr)

    def pop(self) -> None:
        if len(self.arr) != 0:
            self.arr.pop()
        if len(self.arr) != 0:
            self.m = min(self.arr)

    def top(self) -> int:
        if len(self.arr) != 0:
            return self.arr[-1]

    def getMin(self) -> int:
        return self.m