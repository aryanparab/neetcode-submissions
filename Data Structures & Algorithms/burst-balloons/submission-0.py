class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # if i burst ith ballon, i will have
        # nums[:i]+nums[i+1] new array and coins 

        def bursty(arr,coins):
            if len(arr)==1:
                
                return coins + arr[0]
            mx = 0 
            for i in range(len(arr)):
                new_arr = arr[:i]+arr[i+1:]
                cc = coins
                if i==0:
                    cc += arr[i]*arr[i+1]
                elif i==len(arr)-1:
                    cc+=arr[i]*arr[i-1]
                else:
                    cc+=arr[i-1]*arr[i]*arr[i+1]
                mx = max(mx,bursty(new_arr,cc))
            
            return mx
        return bursty(nums,0)