class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        mid = length // 2 + length % 2 - 1

        if nums[mid] == target:
            return mid

        if nums[length-1] == target:
            return length-1
            
        step = 1 if nums[mid] > nums[length-1] and (target < nums[length-1] or target > nums[mid]) else -1
        stop = -1 if step == -1 else length
        for i in range(mid, stop, step):
            if nums[i] == target:
                return i
        
        return -1
        