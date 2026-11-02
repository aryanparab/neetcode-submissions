class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))
            else:
                
                x1,x2 = stack.pop(),stack.pop()
                
                if i=="+":
                    x3 = x1+x2
                elif i=="-":
                    x3 = x2-x1
                elif i=="*":
                    x3 = x1*x2
                else:
                    x3 = int(float(x2)/x1)
                stack.append(x3)
            
        return stack[0]
