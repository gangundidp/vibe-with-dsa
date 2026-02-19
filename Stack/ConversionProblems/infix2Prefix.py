# Function to return precedence of operators
def getPriority(C):
    if C == '^':  # Exponent operator has highest precedence
        return 3
    elif C == '*' or C == '/':  # Multiplication and division have higher precedence than addition
        return 2
    elif C == '+' or C == '-':  # Addition and subtraction have lowest precedence
        return 1
    return 0

# Function to convert infix expression to postfix expression
def infixToPostfix(infix):
    infix = '(' + infix + ')'  # Add parentheses to handle edge cases
    stack = []  # Stack to store operators
    result = ""  # String to store the resulting postfix expression

    for c in infix:
        # If the scanned character is an operand, add it to output
        if c.isalnum():
            result += c

        # If the scanned character is ‘(’, push it to the stack
        elif c == '(':
            stack.append('(')

        # If the scanned character is ‘)’, pop from stack until an ‘(‘ is encountered
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # Remove '(' from the stack

        # If an operator is found
        else:
            while stack and getPriority(c) <= getPriority(stack[-1]):
                result += stack.pop()
            stack.append(c)  # Push current operator on stack

    # Pop all remaining elements from the stack
    while stack:
        result += stack.pop()

    return result  # Return the postfix expression

# Function to convert infix expression to prefix expression
def infixToPrefix(infix):
    infix = infix[::-1]  # Reverse the infix expression

    # Replace '(' with ')' and vice versa
    infix = infix.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    # Get the postfix of the modified string
    prefix = infixToPostfix(infix)

    # Reverse the postfix to get the prefix
    return prefix[::-1]  # Return the prefix expression

# Driver code
if __name__ == "__main__":
    exp = "(p+q)*(c-d)"  # Infix expression
    print(f"Infix expression: {exp}")
    print(f"Prefix Expression: {infixToPrefix(exp)}")  # Output the prefix expression