class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largest_sum = float('-inf')
        running = float('-inf')
        for num in nums:
            if num > running + num:
                running = num   #start over; prev stuff no use
            else:
                running += num
            largest_sum = max(largest_sum, running)
        return largest_sum

lis = [-2,1,-3,4,-1,2,1,-5,4]

sol = Solution()
print(sol.maxSubArray(lis))