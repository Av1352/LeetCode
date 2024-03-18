class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        loot1, loot2 = 0, 0
        for i in nums:
            temp = max(loot1 + i, loot2)
            loot1 = loot2
            loot2 = temp
        return loot2

if __name__ == "__main__":
    a = Solution()
    n = [1,2,3,1]
    print(a.rob(n)) 