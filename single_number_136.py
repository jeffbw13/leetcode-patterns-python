class Solution:
    # why did I have to lowercase "List" below?
    def singleNumber(self, nums: list[int]) -> int:
        cache = {}
        for num in nums:
            if num in cache:
                cache[num] = cache[num] + 1
            else:
                cache[num] = 1

        #print(cache)
        for k, v in cache.items():
            if v == 1:
                return k

sol = Solution()
print(sol.singleNumber([1,2,2,3,3]))
