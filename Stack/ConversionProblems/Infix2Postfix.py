class Solution:
    def infixToPostfix(self, s: str):
        st = []
        ans = ""

        for ch in s:
            # if (ch <= "A" and ch >= "Z") or (ch <= "a" and ch >= "z") or (ch <= '0' and ch >= '9'):
            if ch.isalnum():
                ans += ch
            elif (ch == "("):
                st.append(ch)
            elif (ch == ")"):
                while (st and st[-1] != "("):
                    ans += st.pop()
                st.pop()
            else:
                while st and self.priority(ch) <= self.priority(st[-1]):
                    ans += st.pop()
                st.append(ch)
            
        while st:
            ans += st.pop()
        
        print("Postfix Expression: ", ans)
    
    def priority(self, x):
        if x == "^":
            return 3
        elif x == "/" or x == "*":
            return 2
        elif x == "+" or x == "-":
            return 1
        return -1
    
if __name__ == "__main__":
    sols = Solution()
    
    exp = "(p+q)*(m-n)"  # Infix expression
    print(f"Infix expression: {exp}")
    sols.infixToPostfix(exp)
            
                    
            
        