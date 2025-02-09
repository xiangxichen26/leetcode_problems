class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
            return
        self.prefix.append(self.prefix[-1] * num)  

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            # 不足 k 个元素，是因为最后 k 个元素存在 0
            return 0
        # 计算最后 k 个元素积
        return self.prefix[-1] // self.prefix[-k-1]


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)