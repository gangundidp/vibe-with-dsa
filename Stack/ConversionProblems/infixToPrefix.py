class Solution:
    def infixToPrefix(self, s: str):
        st = []
        ans = ""
        infix = s[::-1]
        
        for ch in infix:
            if ch.isalnum():
                ans += ch
            elif ch == ")":
                st.append(ch)
            elif ch == "(":
                while st and st[-1] != ")":
                    ans += st.pop()
                st.pop()
            else:
                while (st and self.prio(ch) < self.prio(st[-1])) or (st and ch == st[-1] and ch == "^"):
                    ans += st.pop()
                st.append(ch)
                
        while st:
            ans += st.pop()
            
        print("Prefix Expression: ", ans[::-1])
            
    def prio(self, x):
        if x == "^":
            return 3
        elif x == "/" or x == "*":
            return 2
        elif x == "+" or x == "-":
            return 1
        return -1
    
    def isRightAssociative(self, op):
        return op == "^"

    
if __name__ == "__main__":
    sols = Solution()
    
    infix = "x+y*z/w+u"
    print("Infix Expression: ", infix)
    sols.infixToPrefix(infix)
    
    infix = "a+b"
    print("Infix Expression: ", infix)
    sols.infixToPrefix(infix)
    
    infix = "a+b-c"
    print("Infix Expression: ", infix)
    sols.infixToPrefix(infix)
     
    infix = "(p+q)*(c-d)"
    print("Infix Expression: ", infix)
    sols.infixToPrefix(infix)
     
    infix = "(p^q)*(c^d)"
    print("Infix Expression: ", infix)
    sols.infixToPrefix(infix)
     
    infix = "(p^q)^(c^d)"
    print("Infix Expression: ", infix)
    sols.infixToPrefix(infix)
     
    infix = "a^b^c"
    print("Infix Expression: ", infix)
    sols.infixToPrefix(infix)
    