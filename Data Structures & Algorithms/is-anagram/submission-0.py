class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        arr =[0]*26
        for i in range(len(s)):
            x,y= ord(s[i].lower())-97,ord(t[i].lower())-97
            arr[x]+=1
            arr[y]-=1
        x= 0
        for i in arr:
            x+=abs(i)
        return True if x==0 else False