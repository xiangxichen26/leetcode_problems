class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if not nums or indexDiff <= 0:
            return False

        window = SortedList()  # 维护一个有序窗口

        for i, num in enumerate(nums):
            # 在窗口内查找满足 abs(nums[i] - x) <= valueDiff 的 x
            pos = window.bisect_left(num - valueDiff)

            # 检查 pos 位置是否存在符合条件的数
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True

            # 插入当前数字
            window.add(num)

            # 维护窗口大小，超出 indexDiff 的范围，删除最早的元素
            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])

        return False
