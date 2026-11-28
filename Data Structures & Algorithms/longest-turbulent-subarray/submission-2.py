class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<2:
            return len(arr)
        
        ans = 1
        current = 1 if arr[0] == arr[1] else 2
        ans = max(ans, current)

        prev = 0 if arr[0] == arr[1] else (1 if arr[0] < arr[1] else -1)
        for i in range(2,len(arr)):
            if arr[i]>arr[i-1] and prev == -1:
                current+=1
                prev*=-1
            elif arr[i]<arr[i-1] and prev == 1:
                current+=1
                prev*=-1
            elif arr[i] == arr[i - 1]:
                current = 1
                prev = 0
            else:
                
                current = 2
                prev = -1 if arr[i] > arr[i - 1] else 1
                
                prev = 1 if arr[i-1]<arr[i] else -1


            
            ans = max(current,ans)
        return ans


            