class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_ans(houses):
            
            if len(houses)<=2:
                return max(houses)
            if len(houses)==3:
                return max(houses[1],houses[0]+houses[2])
            temp = [0 for _ in range(len(houses))]
            temp[0],temp[1],temp[2] = houses[0],houses[1],houses[2]+houses[0]
            for i in range(3,len(houses)):
                temp[i] = max(temp[i-1],houses[i]+temp[i-2],houses[i]+temp[i-3])
           
            return temp[-1]
        if len(nums)<=1:return max(nums)
        return max(get_ans(nums[1:]),get_ans(nums[:len(nums)-1]))