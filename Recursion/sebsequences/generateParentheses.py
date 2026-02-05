def generateParentheses(n, curr: str, res):
    if curr.count('(') < curr.count(')'):
        return
    
    if len(curr) == 2*n:
        if curr.count('(') == curr.count(')'):
            res.append(curr)
        return
    
    generateParentheses(n, curr + '(', res)

    if not curr or curr.count('(') != curr.count(')'):
        generateParentheses(n, curr + ')', res)

def main():
    n = int(input("n: "))
    res = []
    generateParentheses(n, '', res)
    print("Output: ", res)

main()