class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        uniqueNums = set(nums)
        if len(nums) == len(uniqueNums):
            return False
        else:
            return True

lis = [3,1,5,7,5,9]

sol = Solution()
print(sol.containsDuplicate(lis))