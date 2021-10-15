class NumArray:
    # this appears to be all about OO
    nums = []
    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        totl = 0
        for x in range(max(0, left), min(right+1, len(self.nums)+1)):
            totl += self.nums[x]
        return totl

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

na = NumArray([-2,0,3,-5,2,-1])
print(na.sumRange(0,2),na.sumRange(2,5),na.sumRange(0,5))

