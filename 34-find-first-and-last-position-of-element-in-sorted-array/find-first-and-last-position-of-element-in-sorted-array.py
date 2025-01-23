class Solution:
    def findLeftBound(self, arr:List[int], value: int) -> int:
            left = 0 
            right = len(arr)

            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] == value:
                    right = mid
                elif arr[mid] < value:
                    left = mid + 1
                elif arr[mid] > value:
                    right = mid
            
            return left
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # sorted array -non decreasing
        # Time logn
        # find left and right bound
        
        left = self.findLeftBound(nums,target)
        right = self.findLeftBound(nums,target+1) - 1

        if left >= 0 and left<=right:
            return [left,right]
        else:
            return [-1,-1]        

