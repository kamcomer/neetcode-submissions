class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, last, sol):
            if last == target:
                res.append(sol.copy())
                return
            if i >= n or last > target:
                return

            sol.append(nums[i])
            new_last = last+nums[i]
            dfs(i, new_last, sol)
            sol.pop()
            dfs(i+1, last, sol)

        dfs(0, 0, [])

        return res
            
