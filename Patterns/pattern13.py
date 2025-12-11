def pattern13(n):
    i = 1
    for row in range(n):
        for col in range(row+1):
            print(i, end=' ')
            i += 1
        print()
        
        
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern13(n)