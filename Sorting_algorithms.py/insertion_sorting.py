def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0:
            if lst[j] < lst[j-1]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
            j -= 1
    return lst

if __name__ == "__main__":
    lst = [39, 903, -49, 0, 3]
    print(insertion_sort(lst))