def pattern19(n):
    for row in range(2*n):
        stars_left, spaces, stars_right = n-row, 2*row , n-row
        if (row > 4):
            stars_left, spaces, stars_right = row-n+1, (2*n)-(row//2), row-n+1
            print(stars_left, spaces, stars_right)
        for i in range(stars_left):
            print('*', end=' ')
        
        for j in range(spaces):
            print(' ', end=' ')
        
        for k in range(stars_right):
            print('*', end=' ')
        print()

if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern19(n)