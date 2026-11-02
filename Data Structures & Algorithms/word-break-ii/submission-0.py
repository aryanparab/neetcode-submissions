class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def word(i,ss):
            if i==len(s):
                ans.append(ss.strip())
            x = ""
            while i < len(s):
                x+=s[i]
                i+=1
                if x in wordDict:
                    word(i,ss+x+" ")
            return
        wordDict = set(wordDict)
        ans = []
        word(0,"")
        return ans