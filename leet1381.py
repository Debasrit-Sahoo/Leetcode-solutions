class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0]*maxSize
        self.used = 0
        self.max = maxSize

    def push(self, x: int) -> None:
        if self.used == self.max: return
        self.stack[self.used] = x
        self.used+=1

    def pop(self) -> int:
        if self.used == 0: return -1
        self.used -= 1
        return self.stack[self.used]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.used)):
            self.stack[i] += val
