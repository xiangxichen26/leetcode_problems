class MRUQueue:

    def __init__(self, n: int):
        self.size = 0
        self.mRUQueue = []
        for i in range(1,n+1):
            self.mRUQueue.append(i)
            self.size += 1

    def fetch(self, k: int) -> int:
        if k > self.size or k < 1:
            return
        
        x = self.mRUQueue[k-1]
        self.mRUQueue[k-1: self.size-1] = self.mRUQueue[k:]
        self.mRUQueue[self.size-1] = x
        return x


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)