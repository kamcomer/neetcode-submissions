class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder_map = {}
        for i in range(len(nums)):
            num = nums[i]
            rem = target-num
            if rem in remainder_map:
                return [remainder_map[rem], i]
            
            remainder_map[num] = i

        

        