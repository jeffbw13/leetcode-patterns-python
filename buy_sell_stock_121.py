class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        highest = 0
        low = 9999999999
        for price in prices:
            low = min(low, price)
            if price > low:
                diff = price - low
                if diff > highest:
                    highest = diff

        return highest

lis = [7,1,5,3,6,4]
sol = Solution()

print(sol.maxProfit(lis))