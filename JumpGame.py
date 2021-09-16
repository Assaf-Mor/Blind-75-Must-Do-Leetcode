class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        currentlast = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= currentlast:
               currentLast = i
        
        return True if currentLast == 0 else False