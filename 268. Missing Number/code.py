class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected = sum(range(len(nums) + 1))
        actual = sum(nums)

        return expected - actual

if __name__ == "__main__":
    a = Solution()
    nums = [3,0,1]
    print(a.missingNumber(nums))  