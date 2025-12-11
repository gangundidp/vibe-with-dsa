def pattern5(n):
    for row in range(n):
        for col in range(n - row):
            print('*', end=' ')
        print()
        
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern5(n)
    