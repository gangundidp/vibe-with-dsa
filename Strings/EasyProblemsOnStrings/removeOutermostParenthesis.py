class Solution:
    '''
    Problem Statement: A valid parentheses string is defined by the following rules:

    It is the empty string "".
    If A is a valid parentheses string, then so is "(" + A + ")".
    If A and B are valid parentheses strings, then A + B is also valid.

    A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.

    Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return 
    the resulting string.
    '''
    def removeParenthesis(self, string):
        result = ''
        levelCounter = 0
        
        for char in string:
            if char == '(':
                levelCounter += 1
                if levelCounter > 1:
                    result += '('
            else:
                levelCounter -= 1
                if levelCounter > 0:
                    result += ')'
        return result
    
if __name__ == "__main__":
    sols = Solution()
    # string = input('Enter string: ')
    string = "((()))"
    print("Output: ", sols.removeParenthesis(string))
    string = "()(()())(())"
    print("Output: ", sols.removeParenthesis(string))