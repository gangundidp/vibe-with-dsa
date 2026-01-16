def reverseStack(stack, start, end):
    if start > end:
        return
    
    stack[start], stack[end] = stack[end], stack[start]

    reverseStack(stack, start + 1, end - 1)

if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    reverseStack(stack, 0, len(stack)-1)
    print('Reversed stack: ', stack)

    stack = [12, 3, 5, 4, 5]
    reverseStack(stack, 0, len(stack)-1)
    print('Reversed stack: ', stack)