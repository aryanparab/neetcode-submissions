import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = []
        v = {'a': a, 'b': b, 'c': c}
        for i, j in v.items():
            if j == 0: 
                continue
            heapq.heappush(hp, [-j, i])
        
        ans = ""
        while hp:
            count, char = heapq.heappop(hp)
            

            if len(ans) >= 2 and ans[-1] == char and ans[-2] == char:
                if not hp:
                    return ans  
                next_count, next_char = heapq.heappop(hp)
                
               
                ans += next_char
                next_count += 1
                

                if next_count != 0:
                    heapq.heappush(hp, [next_count, next_char])
                

                heapq.heappush(hp, [count, char])
            else:
              
                ans += char
                count += 1
                if count != 0:
                    heapq.heappush(hp, [count, char])
                    
        return ans