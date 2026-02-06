def countSetBits(num):
    count = 0
    
    while num > 0:
        if (num & (1 << 0)):
            count += 1
        num = num >> 1
        
    return count

if __name__ == "__main__":
    num = int(input("num: "))
    print("Output: ", countSetBits(num))
    
    
'''
------------------------ Algorithm ---------------------
Initialize a counter to zero.
While the number is greater than zero:
    Check if the least significant bit (LSB) is 1 by performing bitwise AND with 1.
    If LSB is 1, increment the counter.
    Right shift the number by one bit.
Return the counter.

n = 3
binary of 3 = 011

3 > 0:
    last bit of 011 is 1, increment count +1 (num & (1 << 0))
    set n = n >> 1, means 011 -> 001
1 > 0:
    last bit of 001 is 1, increment count +1 (num & (1 << 0))
    set n = n >> 1, means 001 -> 000
0 > 0:
return count (i.e. 2)

'''