class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sortedNums = list(nums)
        for num in nums:
            try:
                sortedNums[num] = num
            except:
                three = 1 + 2
        #print(sortedNums, len(sortedNums))
        for x in range(len(sortedNums)):
            #print(x)
            if x != sortedNums[x]:
                return x
        return len(sortedNums)

lis = [3,0,1]

sol = Solution()
print(sol.missingNumber(lis))