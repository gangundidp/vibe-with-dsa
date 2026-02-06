def checkPowOf2(num):
    return (num & (num - 1)) == 0

if __name__ == "__main__":
    num = int(input("num: "))
    if checkPowOf2(num):
        print(f'{num} is power of 2')
    else:
        print(f'{num} is not power of 2')
        
'''
================= Algorithm ========================
Power of two numbers have exactly one bit set in their binary form.
Subtracting one flips all bits after the set bit, creating no overlap with the original number.
A bitwise AND between the number and one less than itself will be zero only for powers of two.
This property allows for a fast check without looping or dividing.

n = 16
Binary of 16 = 10000
n-1 = 15
Binary of 15 = 01111

    10000 
  & 01111
    -----
    00000
'''