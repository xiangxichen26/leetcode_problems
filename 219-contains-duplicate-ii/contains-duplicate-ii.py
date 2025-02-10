class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 0
        window = set()

        if k==0:
            return False


        while right < len(nums):
            
            if nums[right] in window:
                return True
            window.add(nums[right]) 
            right += 1

            while left < right and right-left > k:
                window.remove(nums[left])
                left += 1
        
        return False