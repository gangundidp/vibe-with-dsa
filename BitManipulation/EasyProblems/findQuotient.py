def findQuotient(dividend, divisor): # O(quotient)
    '''
    Problem Statement: Given the two integers, dividend and divisor.
    Divide without using the mod, division, or multiplication operators and return the quotient.

    The fractional portion of the integer division should be lost as it truncates toward zero.

    As an illustration, 8.345 and -2.7335 would be reduced to 8 and -2 respectively.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
    '''
    if dividend == divisor:
        return  1
    
    if dividend == -2**31 and divisor == -1:
        return (2**31)-1
    
    if divisor == 1:
        return dividend
    
    isPositive = True
    if dividend >= 0 and divisor < 0:
        isPositive = False
    elif dividend < 0 and divisor > 0:
        isPositive = False
       
    # Converting as absolute values 
    dividend = abs(dividend)
    divisor = abs(divisor) 
    cnt = 0
    sum = 0
    
    while ((sum + divisor) <= dividend):
        sum += divisor
        cnt += 1
        
    if cnt > 2**31-1 and isPositive:
        return 2**31-1
    elif cnt > 2**31-1 and not isPositive:
        return -2**31
    
    return cnt if isPositive else -1 * cnt

# if __name__ == '__main__':
#     dividend = int(input("Dividend: "))
#     divisor = int(input("Divisor: "))
#     print("Quotient: ", findQuotient(dividend, divisor))
    
def findQuotientBitManipulation(dividend, divisor):
    if dividend == divisor:
        return  1
    
    if dividend == -2**31 and divisor == -1:
        return (2**31)-1
    
    if divisor == 1:
        return dividend
    
    isPos = True
    if dividend >= 0 and divisor < 0:
        isPos = False
    elif dividend < 0 and divisor > 0:
        isPos = False
        
    n = abs(dividend)
    d = abs(divisor)
    
    ans = 0
    while (n >= d):
        cnt = 0
        while (n >= (d * (2**(cnt+1)))): # (n >= (d << (cnt + 1)))
            cnt += 1
        ans += 2**cnt # ans += (1 << cnt)
        n = n - (d * (2**(cnt))) # n = n - (d * (1 << cnt))

    if ans > 2**31-1 and isPos:
        return 2**31-1
    elif ans > 2**31-1 and not isPos:
        return -2**31
    
    return ans if isPos else -1 * ans


if __name__ == '__main__':
    dividend = int(input("Dividend: "))
    divisor = int(input("Divisor: "))
    print("Quotient: ", findQuotientBitManipulation(dividend, divisor))