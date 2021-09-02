class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftPointer = 0
        rightPointer = len(height) -1
        maxErea = 0
        while leftPointer < rightPointer:
            h = min(height[rightPointer], height[leftPointer])
            maxErea = max(h * (rightPointer - leftPointer), maxErea)
            if(min(height[rightPointer], height[leftPointer])== height[rightPointer]):
                rightPointer -= 1
            else:
                leftPointer += 1
        return maxErea
