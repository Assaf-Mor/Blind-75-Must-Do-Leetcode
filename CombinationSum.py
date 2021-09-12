class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = [] # init the result set
        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i + 1, current, total)
        dfs(0, [], 0)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,3,6,7],7))