class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:return 0
        
        ss = list(set(nums))
        ss.sort()
        if len(ss)==2:
            if ss[0]+1 ==ss[1]:
                return 2
            return 1
        
        mx = 1
        curr= 1
        print(ss)
        for i in range(1,len(ss)):
            if ss[i-1]+1 == ss[i]:
                curr+=1
                #print(ss[i],curr)
            else:
                curr=1
            mx = max(mx,curr)
        return mx