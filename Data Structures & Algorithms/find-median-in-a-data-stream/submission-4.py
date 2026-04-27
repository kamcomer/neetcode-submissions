class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        l,r = 0, len(self.nums)

        while l < r:
            mid = (r+l) // 2

            if self.nums[mid] < num:
                l = mid + 1
            else:
                r = mid
        self.nums.insert(l, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2
        if n % 2:
           return self.nums[mid]

        return (self.nums[mid-1] + self.nums[mid]) / 2
        
        