class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n  = len(nums)
        ans = []
        def addi(visited,current):
            if len(current)==n:
                ans.append(current.copy())
                return
            for i in range(n):
                if i not in visited:
                    current.append(nums[i])
                    visited.add(i)
                    addi(visited,current)
                    visited.remove(i)
                    current.pop(-1)
            return 
        addi(set(),[])
        return ans
        