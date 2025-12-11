def selectionSort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

if __name__ == "__main__":
    lst = [3,89,9048,2]
    print(selectionSort(lst))
