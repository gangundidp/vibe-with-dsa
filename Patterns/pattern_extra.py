def pattern_extra(n):
    for row in range(n):
        spaces_left, stars_center, spaces_right = (n - row - 1), (2*row) + 1, (n - row - 1)
        if(row >= 5):
            spaces_left, stars_center, spaces_right = row, (2*n) - (2*row) - 1, row
        for row in range(n):
            for i in range(spaces_left):
                print(' ', end=' ')
            
            for j in range(stars_center):
                print('*', end=' ')
            
            for k in range(spaces_right):
                print(' ', end=' ')
            print()  
        
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern_extra(n)