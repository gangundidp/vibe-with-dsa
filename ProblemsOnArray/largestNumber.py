def largestNumber(lst):
    largest_number = float('-inf')
    for ele in lst:
        if ele > largest_number:
            largest_number = ele
    return largest_number

if __name__ == "__main__":
    lst = [3, 49, 82, -32, 0]
    print("Largest Number: ", largestNumber(lst))