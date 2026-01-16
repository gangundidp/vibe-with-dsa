def countGoodNumbers(n: int, idx: int, res=1) -> int:
    if idx == n:
        return res % (10 ** 9 + 7)
    
    if idx%2 == 0:
        res = res * 5
    else:
        res = res * 4
    
    return countGoodNumbers(n, idx + 1, res)

MOD = (10 ** 9 + 7)
def countGoodNumbersOptimal(n: int) -> int:
    even_positions = ((n + 1) // 2) * 5
    odd_positions = (n // 2) * 4
    
    return (even_positions * odd_positions) % MOD

if __name__ == "__main__":
    n = int(input("N: "))
    print("Output: ", countGoodNumbers(n, 0))
    print("Output: ", countGoodNumbersOptimal(n))