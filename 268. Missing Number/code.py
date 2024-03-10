class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0, len(nums)+1):
        #     if i not in nums:
        #         return i

        n = len(nums)
        expected = (n*(n+1))/2
        actual = sum(nums)

        return expected - actual

if __name__ == "__main__":
    a = Solution()
    nums = [3,0,1]
    print(a.missingNumber(nums))  