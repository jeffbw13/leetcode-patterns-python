class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        while left <= right:
            #find midpoint
            mid = left + (right - left) // 2
            #print(left, mid, right, nums[mid])
            if nums[mid] == target:
                return mid;
            if target < nums[mid]:   #use mid as high end
                right = mid - 1
            else:
                left = mid + 1

        return -1