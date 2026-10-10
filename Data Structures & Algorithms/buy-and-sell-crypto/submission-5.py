class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = -1
        right = 0
        ult = 0
        while left != right:
            left = right 
            right += 1
            if right == len(prices):
                break
            if left == len(prices): break    
            while prices[left] <= prices[right] :
                dif =  prices[right] - prices[left]
                ult = max(dif,ult)
                
                right += 1
                if right == len(prices): break

        return ult        



