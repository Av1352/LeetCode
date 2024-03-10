class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        minInd = 0

        for i in range(len(prices)):
            if prices[i] < prices[minInd]:
                minInd = i
                minPrice = prices[i]

            current = prices[i] - prices[minInd]
            if current > maxProfit:
                maxProfit = current
        
        return maxProfit
        

if __name__ == "__main__":
    a = Solution()
    prices =[2,4,1]
    print(a.maxProfit(prices))       