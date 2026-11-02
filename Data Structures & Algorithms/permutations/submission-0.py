class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n  = len(nums)
        ans = []
        def addi(visited,current):
            if len(current)==n:
                ans.append(current)
                return
            for i in range(n):
                if i not in visited:
                    current1 = current.copy()
                    current1.append(nums[i])
                    visited.add(i)
                    addi(visited,current1)
                    visited.remove(i)
                
            return 
        addi(set(),[])
        return ans
        