class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        
        dd= set()
        for i in range(len(t)):
            dd.add(t[i])
        done = set()
        i = 0
        res =[len(s)+1,""]
        while i <len(s):
            if s[i] in dd:
                if done == set():
                    l = i
                done.add(s[i])
            if len(done)==len(dd):
                curr_l = i-l+1
                if res[0]>curr_l:
                    res=[curr_l,s[l:i+1]]
                done.remove(s[l])
                l+=1
                while l<i and s[l] not in done:
                    l+=1
            i+=1
        return res[1]

