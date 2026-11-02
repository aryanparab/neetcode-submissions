class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans =[]
        fnl = {}
        for i in range(len(s)):
            
            fnl[s[i]] = i
        curr_max = -1
        prev =0 

        for i in range(len(s)):
            curr_max = max(curr_max,fnl[s[i]])
            
            if curr_max<=i:
                curr_max = i
                ans.append(i-prev+1)
                prev=i+1
        return ans
            