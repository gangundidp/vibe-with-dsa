def pattern15(n):
    for row in range(n):
        step = 0
        for col in range(n - row):
            print(chr(ord('A')+step), end=' ')
            step += 1
        print()
        
        
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern15(n)