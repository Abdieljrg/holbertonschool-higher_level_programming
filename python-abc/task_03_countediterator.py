class CountedIterator(iter):

    def __init__(self, arr):
        """initialize func"""
        self.iterator = iter(arr)
        self.counter = 0

    def __iter__(self):
        """iterator(self)."""
        return self

    def __next__(self):
        """next item sum, raise to stop"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """number of items iterated over."""
        return self.counter
