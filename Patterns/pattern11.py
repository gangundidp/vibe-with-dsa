def pattern11(n):
    for row in range(n):
        for col in range(row+1):
            if ((row%2 == 0) and (col %2 == 0)) or ((row%2 != 0) and (col%2 != 0)):
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

        
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern11(n)