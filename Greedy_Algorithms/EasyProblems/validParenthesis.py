class Solution:
    def isValid(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for c in s:
            if c == '(':
                min_open += 1
                max_open += 1
                
            elif c == ')':
                min_open -= 1
                max_open -= 1
                
            else:  # c == '*', can be '(', ')' or ''
                min_open -= 1      # treat as ')'
                max_open += 1      # or treat as '('

            # If max_open goes negative, too many closing brackets
            if max_open < 0:
                return False

            # min_open can't be negative
            if min_open < 0:
                min_open = 0

        # String is valid if all opens can be closed
        return min_open == 0


if __name__ == "__main__":
    s = input("Enter the string: ").strip()
    sol = Solution()
    
    if sol.isValid(s):
        print("Valid parenthesis")
    else:
        print("Invalid parenthesis")