class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            vol = min(heights[left], heights[right]) * (right - left)
            res = max(vol, res)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return res