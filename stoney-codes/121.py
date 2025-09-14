class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L,R=0,1
        profit=0
        maxProfit=0
        while L<R and R<len(prices):
            profit=prices[R]-prices[L] 
            if profit<=0:
                L=R 
                R=L+1
            else:
                if maxProfit<profit:
                    maxProfit=profit
                    R=R+1
                else:
                    R=R+1
        return maxProfit