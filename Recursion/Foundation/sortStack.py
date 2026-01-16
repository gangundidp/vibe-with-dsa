def insert(stack, temp):
    if not stack or stack[-1] >= temp:
        stack.append(temp)
        return
    
    val = stack.pop()
    insert(stack, temp)

    stack.append(val)

def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insert(stack, temp)

if __name__ == "__main__":
    stack = [4, 2, 1, 3]
    sortStack(stack)

    print("Sorted stack (desc order): ", stack)
    stack = [4, 32, 111, 3]
    sortStack(stack)

    print("Sorted stack (desc order): ", stack)