class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = bin(n).count('1')
        
        return count

if __name__ == "__main__":
    a = Solution()
    print(a.hammingWeight(11111111111111111111111111111101))  