class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        primes = [2,3,5]
        for p in primes:
            while n % p == 0:
                n = n//p
        if n == 1:
            return True
        else:
            return False
        