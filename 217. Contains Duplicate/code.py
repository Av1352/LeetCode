class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set(nums)
        return len(numSet) != len(nums)        
    
if __name__ == "__main__":
    a = Solution()
    nums = [1,2,3,4]
    print(a.containsDuplicate(nums))  