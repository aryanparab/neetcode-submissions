class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:return 0
        nums.sort()
        ss = list(set(nums))
        mx = 1
        curr= 1
        for i in range(1,len(ss)):
            if ss[i-1]+1 == ss[i]:
                curr+=1
                #print(ss[i],curr)
            else:
                curr=1
            mx = max(mx,curr)
        return mx