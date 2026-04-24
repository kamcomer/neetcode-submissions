class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        mid = int(length / 2 + length % 2) - 1

        if nums[mid] == nums[length-1]:
            return nums[mid]
        
        step = 1 if nums[mid] > nums[length-1] else -1
        stop = -1 if step == -1 else length
        for i in range(mid, stop, step):
            if step == 1:
                if nums[i+1] < nums[i]:
                    return nums[i+1]
            else:
                if nums[i-1] > nums[i]:
                    return nums[i]
        
        return None
        