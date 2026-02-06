def checkBit(n, i):
    if (n & (1 << i)):
        return True
    return False

if __name__ == "__main__":
    n = int(input("N: "))
    i = int(input("i: "))
    print("output: ", checkBit(n, i))
