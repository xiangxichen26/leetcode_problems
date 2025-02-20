class MRUQueue:

    def __init__(self, n: int):
        self.size = n
        self.BUCKET_SIZE = int(sqrt(n))
        self.data = [] # [[],[]]
        self.index = [] # The index array stores the starting element of each bucket for efficient access.
        # then split the numbers into different bucket
        for i in range(1, n+1):
            bucket_index = (i-1) // self.BUCKET_SIZE
            # If thebucketIndexexceeds the size ofdata, a new bucket is created.
            if bucket_index == len(self.data):
                self.data.append([])
                self.index.append(i)
            self.data[-1].append(i)

    def fetch(self, k: int) -> int:
        # find the bucket
        bucket_index = self.upper_bound(self.index, k) - 1
        element = self.data[bucket_index][k - self.index[bucket_index]]
        del self.data[bucket_index][k - self.index[bucket_index]]
        # shift index
        for i in range(bucket_index + 1, len(self.index)):
            self.index[i] -= 1
         # add new bucket 
        if len(self.data[-1]) >= self.BUCKET_SIZE:
            self.data.append([])
            self.index.append(self.size)
        self.data[-1].append(element)

        if len(self.data[bucket_index]) == 0:
            del self.data[bucket_index]
            del self.index[bucket_index]

        return element


    def upper_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)