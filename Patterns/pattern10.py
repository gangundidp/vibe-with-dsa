
def pattern10(n):
    i = 0
    for row in range(1, (2*n)):
        stars  = row
        if(row >= n):
            stars = n - i
            i += 1
        for j in range(1, stars+1):
            print('*', end=' ')
        print()    

        
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern10(n)
    