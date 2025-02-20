class MRUQueue:

    def __init__(self, n: int):
        self.mRUQueue = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        # Get the k-th element (1-indexed)
        value = self.mRUQueue.pop(k - 1)
        # Append the element to the end of the queue
        self.mRUQueue.append(value)
        return value


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)