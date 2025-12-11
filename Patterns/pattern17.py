def pattern17(n):
    for row in range(n):
        for i in range(n - row - 1):
            print(' ', end=' ')
        
        step, char = 0, 'A'
        for j in range((2 * row) + 1):
            if (j > ((2*row)+1)//2):
                # print(j > ((2*row)+1)//2)
                step -= 1
                char = chr(ord(char)-step)
                print(char, end=' ')
            else:
                char = chr(ord()+step)
                step = step + 1
                print(char, end=' ')
                        
        for k in range(n - row - 1):
            print(' ', end=' ')
        print()
    
if __name__ == "__main__":
    no_of_test_cases = int(input('Enter no of test cases: '))
    for _ in range(1, no_of_test_cases + 1):
        print(f'Test Case {_}:')
        n = int(input('Enter no of n: '))
        pattern17(n)