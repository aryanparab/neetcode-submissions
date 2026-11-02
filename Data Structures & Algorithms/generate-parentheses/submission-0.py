class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ss= set()

        def st(op,cl,curr):
            if cl>op:return
            if op+cl==2*n:
                if op!=cl:return
                ss.add(curr)
                return
            st(op+1,cl,curr+"(")
            st(op,cl+1,curr+")")
            return
        st(0,0,"")
        return [i for i in ss]