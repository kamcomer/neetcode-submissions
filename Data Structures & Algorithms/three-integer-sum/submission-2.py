class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        snums = sorted(nums)
        prev = None
        for i in range(len(snums)-2):
            if prev == snums[i]:
                continue
            left = i + 1
            right = len(snums) - 1
            while left < right:    
                val = snums[i] + snums[left] + snums[right]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    res.append([snums[i], snums[left], snums[right]])
                    left += 1
                    right -= 1
                    while snums[left] == snums[left-1] and left < right:
                        left += 1
                prev = snums[i]
        return res

                