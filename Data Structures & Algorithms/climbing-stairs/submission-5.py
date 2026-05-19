class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        p1, p2 = 1, 1
        for i in range(n-1):
            temp = p1
            p1 = p1 + p2
            p2 = temp
        return p1
        