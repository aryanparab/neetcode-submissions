class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans =[]
        fnl = {}
        for i in range(len(s)):
            if s[i] not in fnl:
                fnl[s[i]] = [i,i]
            else:
                fnl[s[i]][1] = i
        curr_max = -1
        prev =0 

        for i in range(len(s)):
            curr_max = max(curr_max,fnl[s[i]][1])
            
            if curr_max<=i:
                curr_max = i
                ans.append(i-prev+1)
                prev=i+1
        return ans
            