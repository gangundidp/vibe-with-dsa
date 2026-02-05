def generateBinaryStrings(n, curr, res):
    if len(curr) == n:
        res.append(curr)
        return
    
    generateBinaryStrings(n, curr + '0', res)

    if not curr or curr[-1] != '1':
        generateBinaryStrings(n, curr + '1', res)

    
def main():
    n = int(input("n: "))

    res = []
    
    generateBinaryStrings(n, '', res)

    print("Output: ", res)

main()
        