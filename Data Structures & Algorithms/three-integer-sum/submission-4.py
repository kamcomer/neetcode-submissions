class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        fmap = defaultdict(int)
        for num in nums:
            fmap[num] += 1

        res = []
        for i in range(len(nums)):
            fmap[nums[i]] -= 1
            if i and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, len(nums)):
                fmap[nums[j]] -= 1
                if j - 1 > i and nums[j-1] == nums[j]:
                    continue
                
                target = -(nums[i] + nums[j])
                if fmap[target] > 0:
                    res.append([target, nums[i], nums[j]])

            for j in range(i + 1, len(nums)):
                fmap[nums[j]] += 1

        return res
            

            

                