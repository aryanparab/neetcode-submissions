class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            ss = target-numbers[i]
            for j in range(i+1,n):
                if ss == numbers[j]:
                    return [i+1,j+1]
        return -1