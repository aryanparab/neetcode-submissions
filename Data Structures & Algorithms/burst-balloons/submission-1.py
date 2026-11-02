class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # if i burst ith ballon, i will have
        # nums[:i]+nums[i+1] new array and coins 
        memo  ={ }
        nums = [1]+nums+[1]
        def burst(l,r):
            if l>r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            mx = 0 
            for i in range(l,r+1):
                mx = max(mx,nums[i]*nums[l-1]*nums[r+1]+burst(l,i-1)+burst(i+1,r))
            memo[(l,r)] = mx
            return mx
        return burst(1,len(nums)-2)