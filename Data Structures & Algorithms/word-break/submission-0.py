class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def finder(prev,i):
            if i==len(s):
               
                if s[prev:i] not in wordDict:
                    return False
                return True
            if (prev,i) in memo :
                return memo[(prev,i)]
            x= False
            
            if s[prev:i] in wordDict:
                x= finder(i,i+1)
            memo[(prev,i)] =  x or finder(prev,i+1)
    
            return  memo[(prev,i)]
        
        return finder(0,1)