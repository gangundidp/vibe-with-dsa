def swap(n1, n2):
    n1 = n1 ^ n2
    n2 = n1 ^ n2
    n1 = n1 ^ n2
    
    return n1, n2

if __name__ == "__main__":
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    print("------- After swapping -------")
    print("(n1 and n2): ", swap(n1,n2))

'''
n1 = 3, n2 = 2
n1 = 011 ^ 010 = 001 (1)
n2 = 001 ^ 010 = 011 (3)
n1 = 001 ^ 011 = 010 (2)
'''