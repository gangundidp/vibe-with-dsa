def setRightmostBit(num):
    if (num & ~(num)) == 0:
        return num
    return (num | (num + 1))

if __name__ == "__main__":
    num = int(input("num: "))
    print("Output: ", setRightmostBit(num))
    
'''
----------------------- Alogrithm --------------------------
Use bitwise OR with n + 1:
result = n | (n + 1)
n + 1 flips the rightmost 0 in n to 1, and all bits to the right become 0.
Performing OR sets that bit to 1 while leaving other bits unchanged.

n = 13
bin of 13 = 1101
n + 1 = 1110

Bitwise or (|): 
    1101
    1110
    ----
    1111 -> 15
    
n = 7 (111)
(111 & ~(111)):
    111
    000
    ---
    000 -> 0 
    ans = 7 (all set)
'''