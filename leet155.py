class MinStack:

    def __init__(self):
        self.stk = []
        self.mstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mstk or self.mstk[-1] >= val:
            self.mstk.append(val)

    def pop(self) -> None:
        l = self.stk.pop()
        if self.mstk and l == self.mstk[-1]:
            self.mstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        if self.mstk:
            return self.mstk[-1]