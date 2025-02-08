class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs)
        # 以第一行的列数为基准
        n = len(strs[0])
        for col in range(n):
            for row in range(1, m):
                thisStr, prevStr = strs[row], strs[row - 1]
                # 判断每个字符串的 col 索引是否都相同
                if col >= len(thisStr) or col >= len(prevStr) or thisStr[col] != prevStr[col]:
                    # 发现不匹配的字符，只有 strs[row][0..col-1] 是公共前缀
                    return strs[row][:col]
        return strs[0]
