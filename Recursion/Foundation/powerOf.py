def pow(x, n, res=1):
    if n < 0:
        x = 1/x
        n = -1 * n
    if n == 0:
        return res
    
    res = res * x
    
    return pow(x, n-1, res)

    
def powOptimal(x, n):
    if n == 0:
        return 1
    
    if  n == 1:
        return x
    
    if n < 0:
        return 1 / powOptimal(x, -1 * n)
    
    if n%2 == 0:
        return powOptimal(x * x, n//2)
    else:
        return x * powOptimal(x, n - 1)
    

    
if __name__ == "__main__":
    x = int(input('x: '))
    n = int(input('n: '))
    # print("Output: ", pow(x, n))
    print("Output: ", powOptimal(x, n))