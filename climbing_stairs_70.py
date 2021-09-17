class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci
        if n == 0:
            return 0;
        if n < 2:
            return 1;
        prev = prev_prev = 1
        for num in range(2, n+1):
            fib = prev + prev_prev
            prev_prev = prev
            prev = fib

        return fib

sol = Solution()
print(sol.climbStairs(5))

#  1 1 2 3 5 8