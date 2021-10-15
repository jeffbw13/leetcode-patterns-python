class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = start + (end-start) // 2
            if letters[mid] > target and (mid == 0 or letters[mid-1] <= target):
                return letters[mid]
            if target >= letters[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return letters[0]