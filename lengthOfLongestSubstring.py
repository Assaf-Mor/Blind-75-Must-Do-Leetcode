class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        leftPointer = 0 # the current left most pointer
        maxLength = 0 # the max length of the substring found
        substingSet = set() 
        for rightPointer in range(len(s)):
            while s[rightPointer] in substingSet:
                substingSet.remove(s[leftPointer])
                leftPointer += 1
            substingSet.add(s[rightPointer])
            maxLength = max(maxLength, rightPointer - leftPointer + 1)
        return maxLength
