class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(current):
            x= sum(current)
            if x==target:
                c1 = current.copy()
                c1.sort()
                if c1 not in ans:
                    ans.append(c1)
                return
            if x>target:return 
            for i in nums:
                current.append(i)
                dfs(current)
                current.pop()
            return
        dfs([])
        return ans