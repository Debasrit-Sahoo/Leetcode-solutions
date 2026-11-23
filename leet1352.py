class ProductOfNumbers:
    __slots__ = ('prefix_prod', 'size')
    def __init__(self):
        self.prefix_prod = [1]
        self.size = 1

    def add(self, num: int) -> None:
        if num: self.prefix_prod.append(self.prefix_prod[-1] * num); self.size += 1
        else: self.prefix_prod = [1]; self.size = 0

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix_prod) - 1: return 0
        n = len(self.prefix_prod) - 1
        return self.prefix_prod[-1] // self.prefix_prod[n-k]