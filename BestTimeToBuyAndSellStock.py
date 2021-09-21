class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell = 0, 1
        maxP = 0
        while sell < len(prices) :
            if prices[buy] < prices[sell]:
                maxP = max(maxP, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return maxP
            
        
            
            
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([2,1,4]))