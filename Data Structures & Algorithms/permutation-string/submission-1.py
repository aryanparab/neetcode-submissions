class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        if l > len(s2):
            return False
            
        s1d = {}
        s2d = {}
        
        # 1. Initialize maps
        for i in s1:
            s1d[i] = s1d.get(i, 0) + 1
            s2d[i] = 0
            
        # 2. Populate the very first window
        for j in range(l):
            if s2[j] in s2d:
                s2d[s2[j]] += 1
                
        # 3. Check the first window BEFORE sliding
        if s1d == s2d:
            return True
            
        # 4. Slide the window
        for i in range(l, len(s2)):
            incoming = s2[i]
            outgoing = s2[i - l]
            
            # Increment incoming character
            if incoming in s2d:
                s2d[incoming] += 1
                
            # Decrement outgoing character
            if outgoing in s2d:
                s2d[outgoing] -= 1
                
            # Check after the slide is complete
            if s2d == s1d:
                return True
                
        return False