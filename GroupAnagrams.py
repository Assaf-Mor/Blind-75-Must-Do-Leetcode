from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
               count[ord(c)-ord('a')] +=1
            hash_map[tuple(count)].append(s)
        return hash_map.values()
