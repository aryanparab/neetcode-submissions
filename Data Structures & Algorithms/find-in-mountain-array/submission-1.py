class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        r = mountainArr.length()-1
        while l<r:
            mid = (l+r)//2
            if mountainArr.get(mid)==target:
                return mid
            lv, rv = mountainArr.get(l),mountainArr.get(r)
            if lv>target:
                l= mid+1
            else:
                r= mid-1
        return -1