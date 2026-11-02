class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        curr = []
        if digits=="":return []
        def things(i,s):
            if i==len(digits):
                
                curr.append(s)
                return
            ss = mp[int(digits[i])]
            for j in range(len(ss)):
                things(i+1,s+ss[j])

            return 

        things(0,"")
        return curr
        