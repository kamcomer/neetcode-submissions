class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = curMin = 1
        for num in nums:
            tmp = curMax*num
            curMax = max(tmp, num*curMin, num)
            curMin = min(tmp, num*curMin, num)
            res = max(curMax, res)
        return res


            