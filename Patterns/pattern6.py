def pattern6(n):
    for row in range(n):
        for col in range(1, (n - row) + 1):
            print(col, end=' ')
        print()
        
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern6(n)
    