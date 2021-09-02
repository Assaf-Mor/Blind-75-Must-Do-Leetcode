class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        substring = ""
        maxLen = 0
        
        
        for i in range(len(s)):
            #when palindron is even
            leftPointer = i
            rightPointer = i + 1
            while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                if (rightPointer - leftPointer + 1) > maxLen:
                    substring = s[leftPointer : rightPointer +1]
                    maxLen = rightPointer -leftPointer + 1
                leftPointer -= 1
                rightPointer += 1
            # when palindron is odd
            leftPointer = i
            rightPointer = i
            while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                if (rightPointer - leftPointer + 1) > maxLen:
                    substring = s[leftPointer : rightPointer +1]
                    maxLen = rightPointer -leftPointer + 1
                leftPointer -= 1
                rightPointer += 1

        return substring

