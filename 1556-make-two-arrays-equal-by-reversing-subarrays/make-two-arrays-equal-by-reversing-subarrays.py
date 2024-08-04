class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        n_target = len(target)
        n_arr = len(arr)
        # edge case：
        # if len(target) != len(arr)
        if n_target != n_arr:
            return False
        # if len(target) == len(arr) == 0 
        if n_target ==0 and n_arr == 0:
            return True
        
        target_dict = collections.defaultdict()
        for i in target:
            target_dict[i] = target_dict.get(i,0) + 1

        for i in arr:
            if i not in target_dict or target_dict.get(i) == 0:
                return False
            else:
                target_dict[i] = target_dict.get(i) - 1

        return True

