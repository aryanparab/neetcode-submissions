class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        xx ={}
        for i in strs:
            ss= "".join(sorted(i))
            
            if ss not in xx:
                xx[ss]=[]
            xx[ss].append(i)
        return [i for i in xx.values()]