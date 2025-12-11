def secondLargestNumber(lst):
    largest_number = float('-inf')
    second_largest = float('-inf')
    for ele in lst:
        if ele >= largest_number and ele > second_largest:
            if ele != largest_number:
                second_largest = largest_number
            largest_number = ele
        elif ele > second_largest:
            second_largest = ele
    return second_largest

if __name__ == "__main__":
    lst = [3, 49, 82, -32, 0, 82]
    print("Second Largest Number: ", secondLargestNumber(lst))