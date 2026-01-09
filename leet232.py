class MyQueue:

    def __init__(self):
        self.a, self.b = [], []

    def mov(self):
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        self.mov()
        return self.b.pop()

    def peek(self) -> int:
        self.mov()
        return self.b[-1]

    def empty(self) -> bool:
        return not (self.a or self.b)