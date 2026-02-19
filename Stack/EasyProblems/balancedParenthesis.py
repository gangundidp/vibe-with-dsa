class Solution:
    '''
    Approach
        Whenever we get the opening bracket we will push it into the stack. I.e ‘{‘, ’[’, ’(‘.
        Whenever we get the closing bracket we will check if the stack is non-empty or not.
        If the stack is empty we will return false, else if it is nonempty then we will check if the topmost element of the stack is the opposite pair of the closing bracket or not.
        If it is not the opposite pair of the closing bracket then return false, else move ahead.
        After we move out of the string the stack has to be empty if it is non-empty then return it as invalid else it is a valid string.
    '''
    def isValid(self, str):
        # str = "()[{}()]"
        stack = []
        
        for ch in str:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                
                if (ch == ')' and top == '(') or (ch == ']' and top == '[') or (ch == '}' and top == '{'):
                    continue
                else:
                    return False
                
        return not stack    # True if all brackets matched
    
if __name__ == "__main__":
    sols = Solution()
    
    str = "()[{}()]"
    print("Output: ", sols.isValid(str))
    
    str = "()[}()]"
    print("Output: ", sols.isValid(str))