class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Stack = []
        Dict = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in Dict:
                if Stack and Stack[-1] == Dict[c]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(c)
                
        return True if not Stack else False

