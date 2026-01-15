int_max = 2**31 - 1
int_min = -(2**31)

def helper(ind, num, res, sign):
    if ind >= len(num) or not num[ind].isdigit:
        return sign * res
    
    res = res * 10 + int(num[ind])

    if sign * res <= int_min: return int_min
    if sign * res >= int_max: return int_max
    
    return helper(ind+1, num, res, sign)

def myAtoi(num: str):
    ind = 0
    
    while ind < len(num) and (num[ind] == ' ' or num[ind] == '0'):
        ind += 1
        
    sign = 1
    if ind < len(num) and (num[ind] == '+' or num[ind] == '-'):
        sign = -1 if num[ind] == '-' else 1
        ind += 1
        
    while ind < len(num) and (num[ind] == '0'):
        ind += 1
        
    return helper(ind, num, 0, sign)

if __name__ == "__main__":
    num = input('Enter string: ')
    print('Output: ', myAtoi(num))