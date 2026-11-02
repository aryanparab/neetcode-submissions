class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        digits[-1]=0
        n = len(digits)-2
        while n>-1:
            digits[n]+=1
            if digits[n]==10:
                digits[n]=0
            else:
                break
            n-=1
        if n==-1 :
            digits = [1]+digits
        return digits