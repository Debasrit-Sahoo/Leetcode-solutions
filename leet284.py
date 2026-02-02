class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.cache = None

    def peek(self):
        if self.cache == None:
            self.cache = self.iterator.next()
        return self.cache 

    def next(self):
        if self.cache != None:
            t = self.cache
            self.cache = None
            return t
        return self.iterator.next()
    def hasNext(self):
        return True if self.cache else self.iterator.hasNext()