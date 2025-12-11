def pattern1(rows, cols):
    for row in range(rows):
        for col in range(cols):
            print('*', end=' ')
        print()

if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        rows = int(input('Enter no of rows: '))
        cols = int(input('Enter no of cols: '))
        pattern1(rows, cols)
    