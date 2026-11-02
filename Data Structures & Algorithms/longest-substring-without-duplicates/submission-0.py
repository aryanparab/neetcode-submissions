class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # last_loc = {}
        curr_s = set()
        ans ,l = 0,0
        for i in range(len(s)):
            if s[i] not in curr_s:
                curr_s.add(s[i])
                ans = max(ans,i-l+1)
            else:
                while s[l]!=s[i]:
                    curr_s.remove(s[l])
                    l+=1
                l+=1
           
        return ans


