class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        opt = []
        while asteroids:
            x = asteroids.pop(0)
            while  opt and opt[-1]>0 and x<0 :
                if abs(x)<opt[-1]:
                    x =opt[-1]
                    opt.pop()
                elif abs(x)>opt[-1]:
                    opt.pop()
                elif abs(x)==opt[-1]:
                    opt.pop()
                    x=0
                    break
                
            if x!=0:
                opt.append(x)
            
        return opt

                            
