class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        leftP, rightP = 0, len(nums)-1 #the left and right pointers
        if target < nums[leftP] and target > nums[rightP]: 
            return -1
        
        for i in range(len(nums)): 
            if target == nums[leftP]: 
                return leftP
            elif target > nums[leftP]: 
                leftP += 1
            elif target == nums[rightP]: 
                return rightP 
            elif target < nums[rightP]: 
                rightP -= 1
        return -1