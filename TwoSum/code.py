class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i,j]
            
        
        return []

if __name__ == "__main__":
    a = Solution()
    nums = [2,7,11,15]
    target = 9
    print(a.twoSum(nums, target))