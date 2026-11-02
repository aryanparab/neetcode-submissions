class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ss = set([strs[0][:j] for j in range(len(strs[0])+1)])
        for i in strs:
            temp = set()
            for j in range(1,len(i)+1):
                temp.add(i[:j])
            ss = ss & temp
        nn = ""
        
        for i in ss:
            if len(i)>len(nn):
                nn = i
        return nn