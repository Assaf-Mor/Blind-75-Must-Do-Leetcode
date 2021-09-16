class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxRes = currentMax = 0
        
        for n in nums:
            currentMax += n
            
            if currentMax > maxRes: 
                MaxRes = currentMax
            if currentMax < 0:
                currentMax = 0
                continue
            
                        
        return MaxRes if MaxRes > 0 else max(nums)