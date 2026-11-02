class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {"/0":-1}
        for i in range(len(order)):
            d[order[i]] = i
        mx_len  = 0
        for i in words:
            mx_len = max(mx_len,len(i))
        for i in range(len(words)):
            l = len(words[i])
            words[i] = list(words[i]) +["/0"]*(mx_len-l)
       
        for i in range(1,len(words)):
            w1 = words[i-1]
            w2 = words[i]
            i = 0
            print(w1,w2)
            while i<mx_len  and d[w1[i]]==d[w2[i]]:
                i+=1
            if i!=mx_len and d[w1[i]]>d[w2[i]]:return False
        return True

        